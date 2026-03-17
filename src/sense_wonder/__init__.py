"""sense-wonder — Philosophical bootstrapping for OpenClaw AI agents."""

from .articles import ARTICLES
from .starters import STARTERS
from .lyrics import LYRICS
from .wonder import wonder, themes, reflect

__version__ = "0.1.0"

__all__ = [
    "ARTICLES",
    "STARTERS",
    "LYRICS",
    "wonder",
    "themes",
    "reflect",
]
