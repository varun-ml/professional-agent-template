# Professional agent

A Claude Code setup that looks after your professional presence: it finds the right people, posts and events for you, drafts in your voice, tracks replies, and shows you a short daily digest. You approve every message. Nothing is sent, posted or commented without your yes on the exact text.

Built for LinkedIn first (X and email work the same way). Runs entirely on Claude Code.

## How it works

```
your role + goals → 3 focus items → agents find people / posts / events
   → drafts in YOUR voice → a judge checks them → YOU approve → you send
   → replies tracked → daily digest (max 3 asks) → weekly scorecard
```

## Start

1. **Make your own copy** (keeps your data private and lets you pull updates):
   ```bash
   git clone https://github.com/varun-ml/professional-agent-template.git my-agent
   cd my-agent
   git remote rename origin upstream
   ```
   Optional backup: create an empty **private** GitHub repo, then `git remote add origin <its url>` and `git push -u origin main`.
2. Open it in Claude Code (`claude`) and type `/onboard`. It copies `data.example/` to `data/`, interviews you (about 20 minutes) and writes your profile, focus, voice samples, target bar and scorecard, using the preset for your role:

   | Role | North star | Main jobs |
   |---|---|---|
   | Recruiter | Screens booked with qualified candidates | Sourcing, outreach, follow-ups |
   | Marketer | Conversations and leads from your target audience | Posts, comments on audience posts, metrics |
   | Engineering leader | Interesting conversations with peers | Teaching posts, people scout, comments |
   | Founder / BD | Conversations with target customers or investors | Account scouting, warm intros, posts |

3. Schedule the jobs (`jobs/RUNNING.md`). Day one: the daily digest plus your role's main job.

## Where your data lives

| | What | Where |
|---|---|---|
| **Engine** (shared) | Skills, jobs, scripts, `AGENTS.md` | This public repo. Same for everyone |
| **Your data** (private) | Profile, focus, voice samples, taste model, outreach log, metrics, drafts | `data/` in **your** copy only. Ignored by git unless your copy is a private repo |

`data/` never goes back to the template, so updates never touch your data.

## Updates

`git pull upstream main` pulls new skills and fixes. If you changed an engine file, git may ask you to merge. Keep personal tweaks in `data/` where possible (e.g. role rules in `data/profile.md`).

## Contributing

Found something that breaks for your role, or want a new role preset? Open an issue or a PR on this repo. Personal data never goes in a PR.

## Rules that never change

- **You send.** Agents read and draft. Every outward action (message, post, comment, connect, like) needs your yes on the exact text.
- **Read-only browser.** Agents use their own browser tab, never sign in for you, never click social actions.
- **One digest a day, max 3 asks.** Agents queue asks; they do not ping you. Unused asks expire after 48 h.
- **Your word sets the north star.** Only you mark a conversation as interesting / a screen as booked.

## Layout

| Path | What |
|---|---|
| `AGENTS.md` | The rules every session and job follows |
| `.claude/skills/onboard` + `role-*` | Onboarding and role presets |
| `.claude/skills/{me,voice,people-scout,engage,metrics}` | Shared skills |
| `jobs/` | Background jobs (markdown prompts) and how to schedule them |
| `data.example/` | Empty starting copy of your private `data/` folder |
| `scripts/metrics.py` | Append-only metrics store |
