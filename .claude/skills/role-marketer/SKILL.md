---
name: role-marketer
description: Role preset for marketers, founders doing marketing, and DevRel. Use from /onboard when the user wants audience growth and leads from content, or to retune posting, engagement or the content scorecard.
---

# Role preset: marketer

Fit: one personal voice that builds an audience and turns it into conversations and leads. It drafts posts and comments for you to publish. It does **not** schedule posts, run ads, or manage a company page.

## Questions (after the common interview)
1. Product or brand, in one line; who it is for (the ideal customer profile: role, company size, problem).
2. Where your audience reads (LinkedIn, X, newsletters, communities), and 5 accounts they follow.
3. What you can teach them that's genuinely useful, not about the product: 3 topics you know better than most.
4. Your best 3 posts so far (links), and why you think they worked.
5. What counts as a lead for you: a demo request, a DM asking about the product, a signup, a reply from an ICP person?
6. Posting capacity per week (default 2 posts, plus 5 comments).

## What to write
- **North star**: *conversations or leads from your target audience per week*. Set only on the user's word: `north_star: true` and `north_star_at` on the outreach row, meaning a lead or conversation from your target audience.
- **Scorecard**:
  - impressions (7 days);
  - comments from ICP people per 1,000 impressions, read at day 7;
  - profile visits;
  - DMs from ICP people;
  - leads (★);
  - posts published.
- **Who counts**: the ICP definition. Comments from non-ICP people are counted separately.
- **Outreach stages**: `sent → replied → conversation → lead → customer | no_fit`.
- **data/focus.md**:
  - a content pillar (the teaching topics);
  - engagement with ICP voices;
  - one campaign or launch if there is one.
- **Jobs on**:
  - `inspiration` (daily: up to 3 ICP posts worth a comment, plus ideas);
  - `digest` (daily);
  - `weekly-review`.

  `scout` stays off unless they want 1:1 outreach.

## Drafting rules for this role
- Posts teach one usable thing before any mention of the product. A post that only announces reads as an advert.
- No hashtag strings. No "excited to announce". At most one link, and say why it's worth the click.
- Comments add a mechanism, a number or a counter-example. Never "great post".
- Compare posts only at the same age (e.g. day 7).

## Limits to tell the user
- Metrics are read from the user's own dashboards by a read-only browser tab. Numbers can lag or be windowed differently; the metrics skill labels each window.
- One voice only. A brand voice needs its own samples file and its own onboarding run.
