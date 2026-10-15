---
name: engage
description: Drafting comments and replies on other people's posts for the user, after the user picked which post. Used by the inspiration job and on request.
---

# engage

Only for a post the user picked. Read the full post and any thread under it first.

1. A comment must add one of these: a mechanism, a number from the user's own work, a counter-example, or a sharp question. Never "great post".
2. 1–3 sentences. In the user's voice (`.claude/skills/voice/SKILL.md`).
3. Facts gate: every claim about the user must be traceable to `PROFILE.md`, `data/me/model.md` or their words.
4. Judge with `.claude/skills/voice/judge.md`, plus one more gate. **Value:** would the author want to reply?
5. Show the post, then the comment and the judge table. The user posts it themselves, or the agent posts it only on their yes to the exact text. Log a sent comment in `data/outreach.json`.
