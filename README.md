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

1. Install Claude Code and open this folder: `claude`
2. Run onboarding: type `/onboard`. It interviews you (about 20 minutes) and writes your profile, focus, voice samples, target-people bar and scorecard, using the preset for your role:

   | Role | North star | Main jobs |
   |---|---|---|
   | Recruiter | Screens booked with qualified candidates | Sourcing, outreach, follow-ups |
   | Marketer | Conversations and leads from your target audience | Posts, comments on audience posts, metrics |
   | Engineering leader | Interesting conversations with peers | Teaching posts, people scout, comments |
   | Founder / BD | Conversations with target customers or investors | Account scouting, warm intros, posts |

3. Schedule the jobs (see `jobs/RUNNING.md`). Start with the daily digest only; add the others once it is useful.

## Rules that never change

- **You send.** Agents read and draft. Every outward action (message, post, comment, connect, like) needs your yes on the exact text.
- **Read-only browser.** Agents use their own browser tab, never sign in for you, never click social actions.
- **One digest a day, max 3 asks.** Agents queue asks; they do not ping you. Unused asks expire after 48 h.
- **Your word sets the north star.** Only you mark a conversation as interesting / a screen as booked.

## Layout

| Path | What |
|---|---|
| `AGENTS.md` | The rules every session and job follows |
| `PROFILE.md`, `FOCUS.md` | Who you are; your 3 current focus items (written by onboarding) |
| `.claude/skills/onboard` + `role-*` | Onboarding and role presets |
| `.claude/skills/{me,voice,people-scout,engage,metrics}` | Shared skills |
| `jobs/` | Background jobs (markdown prompts) and how to schedule them |
| `data/` | Your state: outreach log, asks queue, metrics, scorecard, model of your taste, voice samples |
| `scripts/metrics.py` | Append-only metrics store |
