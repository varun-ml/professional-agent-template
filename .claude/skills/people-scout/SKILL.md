---
name: people-scout
description: Finding people for the user from their public work: candidates (recruiter), target accounts and buyers (founder), or peers worth meeting (engineering leader). Used by jobs/scout.md.
---

# people-scout

Read `data/profile.md` ("Who counts") and `data/me/model.md` first. Read the last 50 lines of `data/me/picks.jsonl` (`job: scout`): their picks show who they find worth it, and their skips show who isn't.

## Sweep
Search public sources only: LinkedIn search and posts in your own read-only tab, GitHub, personal blogs, talks, papers, community pages. Skip people the user already knows (1st-degree on LinkedIn, or in `data/contacts.json`).

## Each person must have
Name; current role and company; location; **one specific piece of their own work** with a link (a post, repo, talk or paper), and what it shows; why they clear the bar, quoting the bar line; one thing to talk about; a warm path if one is visible.

## Judge
For each candidate, one fresh judge per lens, run in parallel:
- **Bar:** do they clear data/profile.md's bar? Quote it.
- **Evidence:** does the linked work exist and show what we claim? Open it.
- **Value:** what would the user get from this conversation, in one line?

Cut anyone who fails a lens. If fewer than the target pass, sweep again, using the cut reasons as feedback. At most 3 rounds.

## Output
Write to `data/reports/scout-<date>.md`. Queue **one** ask in `data/asks.json`: "Pick who to contact from scout-<date>". Never contact anyone.
