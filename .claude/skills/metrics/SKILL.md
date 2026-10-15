---
name: metrics
description: Use when reading, reporting or acting on the user's numbers: "how is the post doing", "metrics", "is it working", the weekly review, or before changing posting style.
---

# Metrics

Store: `data/metrics.jsonl`, append-only, one snapshot per line. Write it only through `python3 scripts/metrics.py add`. The summary goes to `data/metrics-summary.json`. The north star comes from `data/outreach.json` (the field the role preset defines). The weekly scorecard goes in `data/scorecard.jsonl`.

## Reading rules
1. Compare posts at the same age (day 7). Say the age.
2. Never count the user's own comments.
3. Under about 1,000 impressions, a change is noise. Say "too early".
4. Before you attribute a change, name the confounders: time of day, media vs text, link in body, edits, visibility setting.
5. Label every number with its window (7 days, 90 days).
6. A fact ("impressions doubled") is not a cause ("because of the hook"). Label inference.

## Report shape
One table: north star and scorecard now, compared with last week and with the start. Then at most 3 lines: what moved, the likely cause (marked as inference), and one thing to try next.
