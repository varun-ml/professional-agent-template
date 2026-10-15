---
name: voice
description: Use before showing the user any draft message, comment or post. Makes drafts sound like the user, built from their real writing in data/voice/samples.md, and ready for the judge in judge.md.
---

# Voice

Drafts must sound like the user's own writing, not like an assistant. The evidence is `data/voice/samples.md` (their real messages and posts, collected at onboarding). Re-read it, and the "Role rules" section of `PROFILE.md` (length limits, follow-up rules), before every draft.

## Measure before drafting
From the samples, note: average sentence length; greeting habit; sign-off habit; language mix; punctuation (count "!"); hedges they use ("I think"); words they never use (the never-use list).

## The shape of a good message
1. The specific thing about the reader: their post, repo, talk, a number from their work. Named, not "your work".
2. One real thing about the user, in their words. Not a bio.
3. One question or one ask. Then stop.

## Always banned (unless the samples show the user uses them)
"hope you're doing well", "would love to", "excited/thrilled to", "reach out", "came across your profile", "caught my attention", stacked hedges ("may potentially"), compliments with no content, titles for themselves in DMs, more than one "!".

## Before showing a draft
Count words; grep the banned list and the never-use list; check there is exactly one ask; mark any claim with no source `[SOURCE?]`. Then send it to a fresh judge with `judge.md`. Show the user the draft only after it passes, along with the judge's table.
