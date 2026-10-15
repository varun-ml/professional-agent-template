# Job: weekly review (Sunday)

1. Read `data/metrics.jsonl` for the week, `data/outreach.json`, `data/asks.json`, `PROFILE.md` (scorecard definition) and `FOCUS.md`.
2. List the threads with 2 or more exchanges this week. **Ask the user** which counted for the north star, and set the field only from their answer, with their words.
3. Append one line to `data/scorecard.jsonl`: the week ending, the north star, and each scorecard number. Unknown stays null.
4. **Asks review:** per job, how many asks it made, showed, had used, expired and had declined. Propose pausing any job with 0 used asks two weeks running.
5. Run the me skill's "update the model" step over the week's corrections.
6. Show the card in chat:
   - the scorecard table;
   - what moved;
   - 3 things for next week;
   - any FOCUS.md change to propose.
