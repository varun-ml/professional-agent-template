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
    import datetime
    snaps = load()
    rows = json.loads(OUTREACH.read_text()) if OUTREACH.exists() else []
    touches = [r for r in rows if r.get("kind") != "post"]
    week_ago = (datetime.date.today() - datetime.timedelta(days=7)).isoformat()
    top = [{"name": "North star, last 7 days", "why": "Defined in data/profile.md; set only on the user's word.",
            "value": sum(1 for r in touches if r.get("north_star") and (r.get("north_star_at") or "") >= week_ago),
            "detail": f"{sum(1 for r in touches if r.get('north_star'))} all time; "
                      f"{sum(1 for r in touches if r.get('status') not in (None, 'sent'))} replies from {len(touches)} touches"}]
    posts = {}
    for s_ in snaps:
        for p in s_.get("posts", []):
            posts[p["url"]] = p
    posts = list(posts.values())
    if posts:  # post metrics only for people who post
        last = snaps[-1]; imp = sum(p["impressions"] for p in posts) or 1
        top += [{"name": "Reach: post impressions, 7 days", "why": "Leading signal for posts.",
                 "value": last["profile"].get("post_impressions_7d"), "detail": f"first snapshot {snaps[0]['at'][:10]}"},
                {"name": "Resonance: comments per 1,000 impressions", "why": "Comments start conversations.",
                 "value": round(1000 * sum(p.get("comments", 0) for p in posts) / imp, 1), "detail": f"{len(posts)} posts"}]
    out = {"at": snaps[-1]["at"] if snaps else None, "top3": top,
           "posts": sorted(posts, key=lambda p: p.get("posted", ""), reverse=True), "snapshots": len(snaps)}
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
