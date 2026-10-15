# Setup playbook (for Claude to follow)

The user may not be an engineer. **You (Claude) do every technical step.** The user only clicks, answers questions and approves. Never ask them to type a command, edit a file or use git. Explain each step in one plain sentence before you do it.

## What the user does first
They open the Claude desktop app → **Code** tab → pick any folder (Documents is fine) and paste:

> Set me up using https://github.com/varun-ml/professional-agent-template/blob/main/SETUP.md

## Step 1: get the copy
1. Check git: `git --version`. If macOS shows an "install developer tools" popup, tell the user: "Click Install on the popup and tell me when it's done (about 5 minutes)." Then check again.
2. If `~/my-agent` already exists, skip to Step 3 (this is an update or a re-run; see "Updates" below).
3. `git clone https://github.com/varun-ml/professional-agent-template.git ~/my-agent`, then `git -C ~/my-agent remote rename origin upstream`.
4. `cp -R ~/my-agent/data.example ~/my-agent/data`. Their data stays only on this Mac. Do not offer a GitHub backup unless they ask.

## Step 2: move into the folder
Tell the user, word for word:
"Your agent is in a folder called **my-agent** in your home folder. Open a new Code session: click **+ New session**, choose the **my-agent** folder, and type **/onboard**. I'll take it from there."

Stop here in this session.

## Step 3: onboarding (in the my-agent session)
`/onboard` interviews them (about 20 minutes, one question at a time) and writes their files. At Step 0 of onboarding, the private-repo question: if they never set up a GitHub backup, answer it yourself ("no") without asking.

## Step 4: Chrome (user clicks, you guide)
The jobs read LinkedIn through their own Chrome. Walk them through it, one step at a time, and wait for "done" after each:
1. Install the **Claude in Chrome** extension from the Chrome Web Store, and connect it to their Claude account.
2. Sign in to LinkedIn in that Chrome themselves. You never sign in or see their password.
3. Test: open your own new tab on linkedin.com/feed, read the page title, close the tab. If it shows a sign-in page, ask them to sign in and retry.

## Step 5: schedule the jobs
For each job with `status: active` in `data/agents.json`:
- If you have a scheduled-tasks tool, create the task yourself: folder `~/my-agent`, prompt `Follow jobs/<job>.md exactly.`, time from the job's `schedule`. Show the user the list before creating it and ask "OK to set these up?".
- If not, guide them through **Code → Scheduled tasks → New task** with the folder, prompt and time filled in for them to copy.

Then run the digest once now, so they see what a day looks like.

## Step 6: tell them how to use it
Say this, in your words, in under 80 words:
- Each day at 10:00 a digest appears in the scheduled task's chat with at most 3 asks.
- Nothing is ever sent or posted for them. They copy a draft and send it themselves, or say "send it" after reading the exact text.
- To change anything ("stop the scout", "I'm now hiring for X", "that person was interesting"), they just say it in a my-agent session.
- To get improvements: they say "update my agent".

## Updates ("update my agent")
1. `git -C ~/my-agent stash` if there are engine-file edits, then `git -C ~/my-agent pull upstream main`, then `git stash pop`.
2. If git reports a conflict, keep their version of anything under `data/`, take upstream for everything else, and tell them in one line what changed.
3. Read the new commits (`git log -5 --oneline`) and tell them in plain words what's new. `data/` is never touched.

## Troubleshooting (say it plainly, fix it yourself)
| Symptom | Fix |
|---|---|
| Job says "signed out" | Ask them to sign in to LinkedIn in Chrome, then rerun |
| Digest never appears | Check the scheduled task exists and the Mac was awake at 10:00; offer to move it to a time they're at the desk |
| "Command not found: git" | Step 1.1 |
| They want to stop everything | Pause each scheduled task; nothing else runs |
