# Running the jobs

Each job is a short instruction file in this folder. Claude runs it on a schedule you set once.

## Before the first run
1. Install the **Claude in Chrome** extension and sign in to LinkedIn (and X, if you use it) in that Chrome. The agents only read there. They never post or sign in for you.
2. Run `/onboard` once. It decides which jobs to turn on and when they run (see `data/agents.json`, `status: active`).

## Set up the schedule (Claude desktop app)
1. Open the Claude desktop app → **Code** → **Scheduled tasks** → **New task**.
2. **Folder:** this repo. **Prompt:** `Follow jobs/digest.md exactly.` **When:** every day at 10:00.
3. Repeat for each other active job (onboarding tells you which, and when; e.g. `jobs/scout.md` daily at 11:30 for a recruiter).
4. Click **Run now** once to test. The digest appears in that task's chat.

## Advanced: cron on a server
`claude -p "Follow jobs/digest.md exactly."` from this folder, on your schedule. Browser jobs need Chrome with the extension on the same machine, so the desktop app is simpler.
