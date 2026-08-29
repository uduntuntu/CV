# CV — agent entry

Shared agent preferences live in the [`.agents`](.agents) git submodule ([uduntuntu/AI](https://github.com/uduntuntu/AI)).

**Follow [`.agents/AGENTS.md`](.agents/AGENTS.md) as the authoritative preferences for this repository** (modes, coding, testing, instruction maintenance). Also use files under `.agents/preferences/` and `.agents/rules/` when relevant.

## This project

- Timeline content: `CV.yaml` (edit data here).
- Generator: `python CV-SVG.py` → `test.svg`.
- Dependencies: `pip install -r requirements.txt`.

Update the submodule after PRs land on `uduntuntu/AI`:

```text
git submodule update --remote .agents
```
