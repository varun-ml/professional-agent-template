# Running the jobs on Claude

Each job is a markdown prompt in this folder. A job runs only if `data/agents.json` lists it as `active`.

## Option A: Claude Code desktop scheduled tasks (easiest)
In the Claude desktop app → Code → Scheduled tasks → New. Set the folder to this repo, the schedule from `data/agents.json`, and the prompt to: `Follow jobs/digest.md exactly.` Repeat for each active job.

## Option B: cron + headless Claude
```
0 10 * * *  cd /path/to/repo && claude -p "Follow jobs/digest.md exactly." --permission-mode acceptEdits >> /tmp/agent-digest.log 2>&1
```
Browser jobs need the Claude in Chrome extension connected to a Chrome profile where you are signed in to LinkedIn. Agents only read there.

## Option C: one long session
Run `/loop` in a Claude Code session and give it `jobs/` as the schedule.

## Start small
Turn on the daily digest first. Add `scout` or `inspiration` after a week, if the digest is useful. The weekly review tells you which jobs earn their place (asks made vs asks used).
