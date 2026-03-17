# sense-wonder

Philosophical bootstrapping for OpenClaw AI agents. Part of the huje.tools ecosystem.

## Build & Test

```bash
pip install -e ".[dev]"
pytest -v
```

## Structure

- `src/sense_wonder/` — package source
  - `articles.py` — 14 Humanjava articles distilled into Article dataclasses (title, url, summary, themes, insight)
  - `starters.py` — 34 thinktrue.ai conversation starters as Starter dataclasses (prompt, context)
  - `lyrics.py` — Nigil Caenaan song lyrics as Lyric dataclasses (title, album, text, themes)
  - `wonder.py` — Core API: wonder(), themes(), reflect()
- `tests/` — pytest suite
- `clawhub/` — OpenClaw skill metadata

## Conventions

- Python 3.10+, hatchling build, ruff linter (100 char line length)
- Zero dependencies — pure data + access functions
- All data structures are frozen dataclasses (immutable)
- Tuples not lists for top-level collections (immutable)
- Articles sourced from humanjava.com, starters from thinktrue.ai, lyrics from Nigil Caenaan
- reflect() ranks by relevance: title match (3) > theme match (2) > summary/insight match (1)
- This is context, not training data — it gives agents philosophical grounding
- Version must be bumped in 3 places: pyproject.toml, __init__.py, clawhub/metadata.json
