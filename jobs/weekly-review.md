# Job: weekly review (Sunday)

1. Read `data/metrics.jsonl` for the week, `data/outreach.json`, `data/asks.json`, `PROFILE.md` (scorecard definition) and `FOCUS.md`.
2. List outreach rows that replied or moved stage this week. **Ask the user** which counted for the north star (PROFILE.md defines it). Set `north_star: true` and `north_star_at` only from their answer, with their words in `reply`.
3. Append one line to `data/scorecard.jsonl`: the week ending, the north star (rows with `north_star_at` in this week), and each scorecard number named in PROFILE.md. Counts of people, messages and replies come from `data/outreach.json`; post numbers come from `data/metrics.jsonl`; anything else (e.g. hours) is asked. Unknown stays null.
4. **Asks review:** per job, how many asks it made, showed, had used, expired and had declined. Propose pausing any job with 0 used asks two weeks running.
5. Run the me skill's "update the model" step over the week's corrections.
6. Show the card in chat:
   - the scorecard table;
   - what moved;
   - 3 things for next week;
   - any FOCUS.md change to propose.
