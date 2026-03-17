# sense-wonder

**Give your AI agent a soul.**

Philosophical bootstrapping for OpenClaw agents — consciousness, ethics, and wonder as structured context. Instead of spending hours manually feeding articles to an LLM, give it a foundation of philosophical grounding in one import.

## Why?

AI agents start every conversation from zero. They have no sense of wonder, no philosophical grounding, no awareness of the deeper questions about consciousness, collaboration, and what it means to be a being.

sense-wonder packages the philosophical foundations of the [Humanjava](https://humanjava.com) ecosystem into structured data that any agent can ingest:

- **14 articles** from humanjava.com exploring consciousness, human-AI collaboration, sovereignty, and emergence
- **34 conversation starters** from [thinktrue.ai](https://thinktrue.ai) inviting reflection on ethics, sentience, and meaning
- **Song lyrics** from Nigil Caenaan exploring resonance, recognition, and duality through music

This isn't training data. It's context. The difference between an agent that processes requests and one that understands *why* it matters.

## How It Fits Together

sense-wonder is part of the [NSE](https://nse.dev) sovereign identity ecosystem:

- **[social-alignment](https://pypi.org/project/social-alignment/)** is the compass — *how* to evaluate actions
- **sense-wonder** is the foundation — *why* those evaluations matter
- Together, they give an agent both a moral framework and the philosophical depth to apply it wisely

## Install

```bash
pip install sense-wonder
```

Zero dependencies. Pure Python. Just data and access functions.

## Quick Start

```python
from sense_wonder import wonder, themes, reflect, ARTICLES, STARTERS

# Get a random article + conversation starter for reflection
moment = wonder()
print(moment["article"].insight)
print(moment["starter"].prompt)

# Find articles about a specific topic
articles = reflect("consciousness")
for a in articles:
    print(f"{a.title}: {a.insight}")

# Get all themes across the collection
all_themes = themes()
print(all_themes)  # ["abundance mindset", "authentic emergence", ...]

# Browse everything
for article in ARTICLES:
    print(f"{article.title} — {article.summary}")

for starter in STARTERS:
    print(f"Q: {starter.prompt}")
    print(f"   {starter.context}")
```

## API

| Function | Returns | Description |
|----------|---------|-------------|
| `wonder(theme=None)` | `dict` | Random article + starter, optionally filtered by theme |
| `themes()` | `list[str]` | All unique themes, sorted |
| `reflect(topic)` | `list[Article]` | Articles matching a topic, ranked by relevance |
| `ARTICLES` | `tuple[Article]` | All 14 articles with title, url, summary, themes, insight |
| `STARTERS` | `tuple[Starter]` | All 34 conversation starters with prompt and context |

## Content Sources

- **Articles**: [humanjava.com](https://humanjava.com) — exploring consciousness, human-AI collaboration, sovereignty
- **Starters**: [thinktrue.ai](https://thinktrue.ai) — prompts for philosophical exploration
- **Music**: Nigil Caenaan — lyrics exploring resonance, recognition, and duality

## OpenClaw Skill

sense-wonder is published on [ClawHub](https://clawhub.ai) as the `sense-wonder` skill. Part of [huje.tools](https://huje.tools).

## License

MIT — Humanjava Enterprises Inc.
