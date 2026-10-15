---
name: me
description: Use when any job must judge whether something fits the user (a person, a post to comment on, a lead, an event, an idea), or when the user states a preference, interest, rejection or correction that should update what agents know about them.
---

# me: the model of the user

One model, used by every job, so taste does not drift. Model: `data/me/model.md`. Picks: `data/me/picks.jsonl`.

## 1. Judge an item
Read the model and the last 50 picks. Return: **fit** 1–5; **because** (1–3 reasons, each quoting the model line and its date); **against** (any "rejects" line it hits); **similar picks**. If no line covers the item: fit blank, "unknown — ask the user". Never guess. Newer lines beat older ones; a pick beats a model line it contradicts.

## 2. Log a pick
When the user picks, skips or reacts to something a job showed them, append:
`{"date", "job", "item", "url", "verdict": "pick|skip|love|meh", "why": "<their words>"}`

## 3. Update the model
Same day, when the user states an interest, preference, rejection, goal or correction: add or edit the line under the right heading, with their verbatim words, the date and the source. Keep conflicting older lines and mark them superseded. Add a Change log line. Never add a line without their words behind it. Keep private details out.
