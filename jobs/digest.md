# Job: daily digest (10:00)

The one place asks reach the user. Read only on every site.

1. Read `AGENTS.md`, `data/profile.md`, `data/focus.md`, `data/outreach.json` and `data/asks.json`.
2. **Replies:** in your own new browser tab, read only, open the LinkedIn messaging list and notifications (X too if data/profile.md lists it). For each outreach row with status `sent` whose person has replied: set `replied`, and add `reply` as a paraphrase of 20 words or fewer. Never open threads you don't need (opening marks them read). Never type or click social actions. If you're signed out, say so and stop. Never sign in.
3. **Numbers:** read the profile dashboard (followers, 7-day impressions) and each own post from the last 14 days (impressions, reactions, comments from others). Pipe one snapshot to `python3 scripts/metrics.py add`.
4. **Asks:**
   - add one ask per reply that needs an answer, and per new commenter;
   - expire past asks;
   - rank the queue with the me skill against data/focus.md;
   - show at most 3.

   An ask that fits no focus item only gets in if it's a live conversation with someone the user marked as north-star, or it has a deadline within 48 h.
5. **Show the digest in chat:**
   - the numbers table, with the change since yesterday;
   - who replied;
   - the top asks, each with its focus item.
6. Close your tab. Set `last_run` for `digest` in `data/agents.json`.

Never set the north-star field yourself.
