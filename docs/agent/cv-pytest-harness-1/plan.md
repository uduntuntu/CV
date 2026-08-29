# Cycle: cv-pytest-harness-1

## Agreement

Introduce a pytest harness for the CV timeline generator: Do makes `CV-SVG.py` importable without side effects (injectable `today` / library-safe `validate_date` / `build_canvas`), adds `pytest` to requirements; Check owns `tests/` + suite (not this Do).

Source plan: `c:\Users\utu\.cursor\plans\cv_testing_harness_39c32b45.plan.md`

## verification

`mixed` — agent runs pytest; human spot-checks one regenerate of real `CV.yaml` → `test.svg`.

## paths

- `pytest`
- `human_practical`

## Plain command

```text
pytest -v tests
```

## Human practical checklist

1. `pip install -r requirements.txt` then `pytest -v tests` — all green.
2. `python CV-SVG.py` still writes a sensible `test.svg` from real `CV.yaml` (open in viewer; rings + arcs present).
3. Confirm personal `CV.yaml` is not copied into `tests/fixtures/`.

## Request-based checklist (default PR body)

- [ ] `CV-SVG.py` import-safe; CLI via `main` unchanged for normal use
- [ ] Date math / canvas build accept injectable `today` (deterministic tests)
- [ ] Invalid dates do not call `input()` on the library path
- [ ] `pytest` in `requirements.txt`; `pytest -v tests` green
- [ ] Fixture YAML only under `tests/fixtures/`; no personal CV content in tests
- [ ] Unit coverage for: validate_date, load_cv, entry_label/entry_layout, days/years/angle, Job/School/Volunteering ids, build_canvas no disk write

## Atomic Do task (this cycle)

On branch `feature/cv-pytest-harness` (from main): refactor `CV-SVG.py` for testability; add `pytest` to `requirements.txt`; write cycle `plan.md`/`do.md` under `docs/agent/cv-pytest-harness-1/`; local commit only. **No** `tests/` edits, no push/PR/merge to main.

## Atomic Check task (later)

Add `tests/` + fixtures; run `pytest -v tests`; package human checklist; PR readiness after green.
