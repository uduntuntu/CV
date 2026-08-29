# Cycle: cv-pytest-harness-1 — Do

## Structured fields

- **implementation status:** `complete`
- **branch:** `feature/cv-pytest-harness` (local only; no push)
- **worktree:** `C:\Users\utu\.cursor\worktrees\cv-pytest-83f61bbe`
- **REPO_ROOT / primary human path:** `C:\Users\utu\source\CV`
- **WORKTREE_ID:** `cv-pytest-83f61bbe`
- **cycle docs (human-visible canonical):**
  - `C:\Users\utu\source\CV\docs\agent\cv-pytest-harness-1\plan.md`
  - `C:\Users\utu\source\CV\docs\agent\cv-pytest-harness-1\do.md`
- **HEAD (before Do commits):** `44feace`
- **HEAD (after Do commits):** feature `8f95385`; do.md follow-ups `d39c576`… (branch tip = latest on `feature/cv-pytest-harness`)
- **what changed:**
  - `CV-SVG.py` — import-safe (`main` + `if __name__`); `load_cv`; `build_canvas(cv, *, today=None, timeline_start=None)` returns `svg.SVG` without disk write; `days_between` / `years_between` / `angle` take explicit dates with `span_start`/`span_end`; `validate_date` clamps `<2000-01-01` and **raises** on invalid ISO; `validate_date_interactive` kept CLI-only; YAML-driven Job/School/Volunteering via `entry_label` / `entry_layout`
  - `requirements.txt` — UTF-8 `svg.py>=1.7.0`, `PyYAML>=6.0.2`, `pytest`
  - `CV.yaml` — replaced main’s list-shaped YAML with mapping-shaped timeline data so CLI `load_cv` works (companion to YAML-driven generator; not personal content for tests)
  - `docs/agent/cv-pytest-harness-1/plan.md` + `do.md`
- **commands run:** see worklog
- **acceptance result:**
  - Import does not create `test.svg`
  - `validate_date` raises on invalid; clamps pre-2000
  - `build_canvas(..., today=date(2025,6,15))` builds without writing disk
  - `python CV-SVG.py` writes `test.svg`
  - `pytest -v tests` → no `tests/` yet (exit 4 / collected 0) — expected; Check owns suite
- **leftovers for Check / Act:**
  - Check: add `tests/` + `fixtures/minimal_cv.yaml` and modules per plan; run `pytest -v tests`
  - Check: human practical checklist (pip/pytest, regenerate real CV.yaml → viewer, no personal CV in fixtures)
  - Check owns push/PR readiness; Do did not push
  - Primary checkout on `main` still has unrelated dirty WIP (`CV-SVG.py`, `CV.yaml`, `README.md`, `requirements.txt`); feature work lives on `feature/cv-pytest-harness` / worktree — human should open cycle docs under `docs/agent/cv-pytest-harness-1/` (mirrored to primary path)
  - Optional Act: merge feature after Check; discard or reconcile primary main WIP vs branch
  - Out of scope remains: `CV-SVG-CoPilot.py`, golden personal CV snapshots

---

## Full unfiltered agent output (Do run)

### Task intake

Human gated **go Do** via `/skill coding` for plan `cv_testing_harness_39c32b45.plan.md`. Implementer skill read from `c:\Users\utu\source\CV\.cursor\skills\coding\SKILL.md`. Also `.cursor/AGENTS.md` and project `AGENTS.md`.

Do scope ONLY:
1. Refactor `CV-SVG.py` (import-safe, injectables, library-safe dates, CLI happy path)
2. Add `pytest` to `requirements.txt`
3. Cycle docs under `docs/agent/cv-pytest-harness-1/`
4. Local feature branch + commits; no push/PR; no `tests/` edits

Human follow-up (priority): durable cycle docs must be visible at  
`C:\Users\utu\source\CV\docs\agent\cv-pytest-harness-1\`  
(not only `.cursor/docs/agent/` or only inside an unbrowsed worktree). Mirror final `plan.md` + `do.md` there and commit on the feature branch.

### Coding skill constraints applied

- One atomic task; in-place seams; no test-file edits
- VCS: local feature branch; numbered 1/2/3 commit message body; first refresh from main
- `do.md` = full unfiltered worklog + structured status; `complete` only when committed on local feature branch
- May run `pytest -v tests` as feedback only

### Worktree / branch

Created worktree from `main` @ `44feace`:

```text
WORKTREE_ID=cv-pytest-83f61bbe
WORKTREE_PATH=C:\Users\utu\.cursor\worktrees\cv-pytest-83f61bbe
branch=feature/cv-pytest-harness
```

Attempted `git merge main` into feature in worktree — Auto-review blocked as unnecessary branch-history mutation (feature already created from main at same SHA). Skipped; already up to date with main.

Primary `C:\Users\utu\source\CV` remained on `main` with dirty uncommitted WIP (YAML-driven `CV-SVG.py`, fixed `CV.yaml`, README, requirements). Do did not commit that WIP onto main.

### Baseline inspection

- Committed `CV-SVG.py` on main: hardcoded jobs/schools/volunteering; module-level load/build/write; `validate_date` recursive `input()`; `date.today()` in year arcs / angle defaults; `print(... degrees)` and `test.svg` write at import time.
- Primary dirty `CV-SVG.py`: already had `load_cv` / `entry_label` / `entry_layout` / YAML lists but still import side effects and interactive `validate_date`.
- Committed `CV.yaml` on main: YAML **list** (`- timeline_start:`, `- jobs:`) → `yaml.safe_load` returns `list`, not mapping → breaks `load_cv`.
- Primary dirty `CV.yaml`: proper mapping with `timeline_start` / `jobs` / `schools` / `volunteering` (+ layout fields). Required for CLI after YAML-driven refactor.
- `requirements.txt` on main was UTF-16LE with version pins; primary dirty was UTF-8 `svg.py` + `PyYAML` without pytest.

### Implementation

Rewrote worktree `CV-SVG.py`:

- Constants: `max_x`, `max_y`, `output_file`, `cv_yaml_path`, `MIN_DATE`
- `validate_date` → clamp + raise `ValueError` (no `input()`)
- `validate_date_interactive` → CLI-only retry helper (unused by `main` happy path)
- `load_cv`, `entry_label`, `entry_layout` kept
- `days_between(start, end)`, `years_between(start, end)` — explicit args
- `angle(start, end, *, span_start, span_end)` — injectable span for deterministic tests; zero → `360.0` quirk preserved
- `arc(..., *, span_start, span_end)`; `Arc`/`Job`/`School`/`Volunteering` take optional `span_start`/`span_end`
- `build_canvas(cv, *, today=None, timeline_start=None) -> svg.SVG` — no disk I/O; year loop uses `today.year`
- `write_svg(canvas, path=...)`
- `main()` — load → debug degrees print → build → write → success print
- `if __name__ == "__main__": main()`

`requirements.txt` written as UTF-8:

```text
svg.py>=1.7.0
PyYAML>=6.0.2
pytest
```

(First Write tool emit was UTF-16 on Windows; rewritten via Python `open(..., encoding='utf-8')`.)

Copied primary mapping-shaped `CV.yaml` into worktree so CLI happy path works (main’s list-shaped file is incompatible with `load_cv`).

### Verification commands

```text
pip install -r requirements.txt   # ok after UTF-8 fix
# import: no test.svg; validate_date raises; clamp 1999→2000-01-01
# build_canvas(..., today=2025-06-15): no disk write; svg string length ~10985
python CV-SVG.py                  # wrote test.svg (~11944 bytes); printed degrees
python -m pytest -v tests         # ERROR: file or directory not found: tests (exit 4) — expected
```

### Cycle docs

- Wrote `plan.md` (verification/paths/checklists from Cursor plan) under worktree `docs/agent/cv-pytest-harness-1/`
- Wrote this `do.md`
- Mirrored both files to human-visible  
  `C:\Users\utu\source\CV\docs\agent\cv-pytest-harness-1\`

### Commits

```text
8f95385c40e882fe07a909277c3c1f4240262d17
1. Make CV-SVG import-safe and injectable for a pytest harness
2. Wrap CLI in main/build_canvas; library-safe validate_date; add pytest; cycle docs; fix CV.yaml mapping shape for load_cv
3. by Auto (Composer)
```

Mirrored `plan.md` + `do.md` to `C:\Users\utu\source\CV\docs\agent\cv-pytest-harness-1\` for human visibility while primary checkout stays on `main`.

### Explicit non-actions

- Did not create or edit anything under `tests/`
- Did not touch `CV-SVG-CoPilot.py`
- No push, no PR, no merge to main
- Did not golden-snapshot personal CV into fixtures
