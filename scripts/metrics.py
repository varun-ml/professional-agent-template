"""Metrics store: append snapshots to data/metrics.jsonl, write data/metrics-summary.json.

  python3 scripts/metrics.py add < snapshot.json   # validate + append one snapshot
  python3 scripts/metrics.py summary                # recompute the top 3 metrics

ponytail: an append-only JSONL file in git is the store. It is versioned, diffable and backed up on push.
Move to SQLite only if queries outgrow a single pass over the file.
"""
import json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG, SUMMARY, OUTREACH = ROOT / "data/metrics.jsonl", ROOT / "data/metrics-summary.json", ROOT / "data/outreach.json"


def load():
    return [json.loads(l) for l in LOG.read_text().splitlines() if l.strip()] if LOG.exists() else []


def add(snap):
    assert isinstance(snap.get("at"), str) and "T" in snap["at"], "at must be an ISO timestamp"
    assert isinstance(snap.get("profile"), dict), "profile must be an object"
    for p in snap.get("posts", []):
        assert p.get("url") and isinstance(p.get("impressions"), int), f"bad post row: {p}"
    if any(s["at"] == snap["at"] for s in load()):
        return  # same snapshot twice: keep one
    with LOG.open("a") as f:
        f.write(json.dumps(snap, ensure_ascii=False) + "\n")


def summary():
    snaps = load()
    if not snaps:
        return {"top3": []}
    first, last = snaps[0], snaps[-1]
    rows = json.loads(OUTREACH.read_text())
    touches = [r for r in rows if r.get("channel") != "linkedin_post"]
    # latest reading of each post
    posts = {}
    for s in snaps:
        for p in s.get("posts", []):
            posts[p["url"]] = p
    posts = list(posts.values())
    imp = sum(p["impressions"] for p in posts) or 1
    out = {
        "at": last["at"],
        "top3": [
            {"name": "North star", "why": "The north star from PROFILE.md, set only on the user's word.",
             "value": sum(bool(r.get("interesting") or r.get("screen_booked") or r.get("lead") or r.get("conversation")) for r in touches),
             "detail": f"{sum(r.get('status') in ('replied', 'met') for r in touches)} replies from {len(touches)} touches"},
            {"name": "Reach: post impressions, 7 days", "why": "Leading signal: are the right people seeing the posts?",
             "value": last["profile"].get("post_impressions_7d"),
             "detail": f"was {first['profile'].get('post_impressions_7d')} on {first['at'][:10]}"},
            {"name": "Resonance: comments per 1,000 impressions", "why": "Comments start conversations; likes do not.",
             "value": round(1000 * sum(p.get("comments", 0) for p in posts) / imp, 1),
             "detail": f"{sum(p.get('reactions', 0) for p in posts)} reactions, {sum(p.get('comments', 0) for p in posts)} comments over {len(posts)} posts"},
        ],
        "posts": sorted(posts, key=lambda p: p.get("posted", ""), reverse=True),
        "snapshots": len(snaps),
    }
    SUMMARY.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    return out


if __name__ == "__main__":
    if sys.argv[1:] == ["add"]:
        add(json.load(sys.stdin)); summary()
    elif sys.argv[1:] == ["summary"]:
        for m in summary()["top3"]:
            print(f"{m['name']}: {m['value']} ({m['detail']})")
    else:
        sys.exit(__doc__)
