---
name: onboard
description: First-run setup. Use when the user types /onboard, when data/profile.md or data/focus.md still contain "<to fill>", or when the user wants to change their role preset. Interviews the user and writes their profile, focus, taste model, voice samples, target bar and scorecard.
---

# Onboard

Goal: in about 20 minutes, turn a blank repo into one that knows who the user is, what they want from being online, who counts for them, and how they write. Ask one question at a time. Use their words verbatim in every file. Never invent facts, titles or goals.

## Step 0: your private data folder
1. If `data/` doesn't exist, copy `data.example/` to `data/` (`cp -R data.example data`).
2. Ask: "Is this copy in a private GitHub repo?" If yes, delete the `data/` line from `.gitignore` so your data is backed up with each commit. If no or unsure, leave it ignored: your data stays on this machine only.
3. Never commit `data/` to a public repo.

## Step 1: pick the role preset
Ask: "Which is closest to what you want this for?"
- **Recruiter**: finding and talking to candidates → `role-recruiter`
- **Marketer**: growing an audience and leads for a product or brand → `role-marketer`
- **Engineering leader**: being known for your work, meeting peers → `role-engineering-leader`
- **Founder / BD**: reaching customers, partners or investors → `role-founder`
- None fits: run the common interview, then ask what a good week looks like and build the north star from that answer.
Load that role skill now and follow it after step 2.

## Step 2: common interview (every role)
1. Your name, role, company, location. Public links (LinkedIn, X, blog, GitHub).
2. In one line, what you do, as you'd say it to a peer.
3. What do you want from this in the next 4 weeks? (Push for something they would notice, not "visibility".)
4. What is off limits: topics, employers, clients, internal details that must never appear in a draft.
5. Voice: paste 5–10 things you actually wrote: messages, posts, comments, emails. Not polished copy. Also: words or phrases you never use.
6. Three people whose online presence you'd like yours to resemble, and one you would not want to sound like. Why?
7. How many hours a week will you give this? (Default 3–5.)

## Step 3: role questions
Run the role skill's questions. It defines the north star, scorecard, calibre bar or persona, outreach stages, which jobs to turn on, and the limits to tell the user.

## Step 4: write the files
- `data/profile.md`: fill every `<to fill>`. North star, scorecard, bar and stages come from the role skill.
- `data/focus.md`: 3 focus items from their 4-week answer and the role defaults. Quote their words.
- `data/me/model.md`: fill each heading from their answers, verbatim with today's date. Leave a heading empty rather than guess.
- `data/voice/samples.md`: their samples verbatim, the never-use list, the people they admire and avoid.
- `data/profile.md` "Role rules": copy the role skill's drafting rules, plus the user's capacity (messages and posts a week), where their targets show their work, and their outreach examples (what got replies, what didn't).
- `data/me/picks.jsonl`: any example people the user named, as `verdict: pick` with their words.
- `data/agents.json`: day one, turn on `digest` plus the role's main job (recruiter and founder: `scout`; marketer and engineering leader: `inspiration`). Set each job's `schedule` from the role skill (a recruiter's scout runs daily). The other jobs stay `planned` until the first weekly review shows the digest is useful.

## Step 5: confirm and first run
1. Show a one-screen summary: north star, 3 focus items, the bar, jobs on, hours a week, what the system will never do.
2. Ask for corrections, apply them, and write each correction into `data/me/model.md`.
3. Explain scheduling (`jobs/RUNNING.md`) and offer to run the daily digest once now.

## Rules
- One question at a time. If an answer is vague, ask once for an example; if still vague, write it as said and mark it "vague — revisit".
- Their words, not yours. No flattering rewrites of their bio.
- Nothing outward during onboarding.
