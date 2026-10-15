# Draft judge

A fresh subagent judges every draft; the writer never judges its own. The judge only judges. It never writes replacement text.

Inputs: the draft, the reader, the purpose (one line), `data/voice/samples.md`, `data/profile.md` (including "Role rules"), `data/me/model.md`.

| Gate | Fails when |
|---|---|
| Purpose | A sentence doesn't serve the one-line purpose |
| Facts | A claim about the reader or the user can't be traced to a file, a public page or the user's words (quote the source) |
| Known | It tells the reader something they already know |
| Domain | The user claims expertise they haven't claimed themselves |
| Tone | A sentence exists to impress; a banned phrase; too many "!" |
| Spoken | The user wouldn't send this line in these words. Quote the closest real line from samples.md |
| Role rules | It breaks a rule in data/profile.md "Role rules" (word limit, one ask, follow-up timing) |
| Shape | The length or the number of messages doesn't match how the user writes to this kind of reader |
| Teaches (posts only) | A peer learns nothing without clicking the link, or the post only announces what the user built |

Output: one table (gates as columns, pass or the failing words), then the smallest fix per failing draft. A draft with any fail does not go to the user; rewrite and re-judge, at most 3 rounds.
