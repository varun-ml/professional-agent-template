---
name: role-recruiter
description: Role preset for recruiters and hiring managers. Use from /onboard when the user is sourcing and engaging candidates, or when a recruiter asks to set up or retune sourcing, outreach or their scorecard.
---

# Role preset: recruiter

Fit: quality sourcing for a few open roles, with personal outreach the recruiter sends themselves. It is **not** a volume tool. You approve every message. LinkedIn does not allow automated sending, and this setup never sends.

## Questions (after the common interview)
1. Open roles right now: title, level, location or remote, must-have skills, nice-to-have, deal-breakers. One at a time; aim for 1–3 roles.
2. For each role: where do great candidates show their work? (GitHub, papers, talks, blogs, specific communities, companies they come from.)
3. What does a great candidate's profile actually look like? Ask for 2 real examples (names or public links) of people they'd hire tomorrow.
4. Your outreach today: paste 3 InMails or DMs that got replies, and 1 that didn't.
5. Your pipeline stages after a reply (e.g. replied → screen booked → submitted → interviewing → offer).
6. Daily sending capacity you're comfortable with (default 10–15 personal messages).

## What to write
- **North star** (PROFILE.md): *screens booked with qualified candidates per week*. Set only by the recruiter's word (`screen_booked: true` on the outreach row).
- **Scorecard**: candidates surfaced; candidates the recruiter approved; messages sent; reply rate; screens booked (★); time to first reply.
- **Calibre bar** (PROFILE.md "Who counts"): the role's must-haves, plus evidence in public work. Each surfaced candidate must cite one specific piece of their work: a repo, a post or a talk.
- **Outreach stages**: `sent → replied → screen_booked → submitted → interviewing → offer → hired | declined`.
- **FOCUS.md**: one item per open role (up to 3).
- **Jobs on**:
  - `scout` (daily, per role, at most 5 candidates each, with evidence);
  - `digest` (daily);
  - `weekly-review`.

  `inspiration` stays off unless they also want an employer brand.

## Drafting rules for this role
- First line names the specific thing of theirs (the repo, the talk, the post). No "I came across your profile".
- One line on the role that matters to *them* (problem, team, stage), not a JD paste.
- One ask: a 15-minute call, or "open to hearing more?". Under 80 words.
- At most one follow-up, after 5 working days.

## Limits to tell the user
- No ATS integration: stages live in `data/outreach.json`. Export as CSV if needed.
- Candidates' private data (phone, email) is not stored unless they shared it in a reply.
- It finds people from public work, so it favours people who publish. Tell the user this bias explicitly.
