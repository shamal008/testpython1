# AGENTS.md — Agent instructions for this workspace

Purpose
- Short, actionable guidance for AI coding agents working in this repository.

Project overview
- Language: Python 3
- Scope: Small educational scripts demonstrating Python basics (`basic.py`, `2basic.py`, `operator.py`).
- No tests, no package structure, no external dependencies.

Run & verify
- Run individual scripts with: `python <filename>.py`.
- There are no automated tests; run scripts manually to inspect output.

Key files
- `basic.py`: data type examples and comments
- `2basic.py`: string and slicing examples
- `operator.py`: placeholder file

Agent guidelines (concise)
- Prefer non-destructive edits. Ask before creating large new files or changing project structure.
- Link to existing documentation rather than copying it. If adding docs, keep them short and link to related files.
- If asked to add runnable examples, include a minimal README and a short `try` command.
- No dependency installs are expected; if a task requires packages, propose a `requirements.txt` and explain why.

Conventions for quick tasks
- Small fixes and clarifications: edit the script in-place and run it to verify output.
- New features or refactors: propose a short plan before implementation.

Contact points for the repo
- Entry scripts: `basic.py`, `2basic.py` — start here to understand patterns.

Where not to overreach
- Do not reorganize into packages or introduce build tooling unless requested.

Notes
- This file is intentionally minimal. For larger projects, create focused instruction files under `.github/` or a dedicated `docs/` folder.
