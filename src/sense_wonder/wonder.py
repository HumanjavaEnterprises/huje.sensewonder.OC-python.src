"""Core API for sense-wonder — access philosophical context."""

import random
from typing import Optional

from .articles import ARTICLES, Article
from .starters import STARTERS, Starter


def wonder(theme: Optional[str] = None) -> dict:
    """Get a random article and starter for philosophical reflection.

    If a theme is provided, returns content matching that theme.
    Otherwise returns a random selection.

    Args:
        theme: Optional theme to filter by (e.g. "consciousness", "partnership").

    Returns:
        Dict with 'article' (Article) and 'starter' (Starter).
    """
    if theme:
        theme_lower = theme.lower()
        matching_articles = [
            a for a in ARTICLES
            if any(theme_lower in t.lower() for t in a.themes)
        ]
        article = random.choice(matching_articles) if matching_articles else random.choice(ARTICLES)
    else:
        article = random.choice(ARTICLES)

    starter = random.choice(STARTERS)

    return {
        "article": article,
        "starter": starter,
    }


def themes() -> list[str]:
    """Get all unique themes across all articles, sorted.

    Returns:
        Sorted list of unique theme strings.
    """
    all_themes: set[str] = set()
    for article in ARTICLES:
        for theme in article.themes:
            all_themes.add(theme)
    return sorted(all_themes)


def reflect(topic: str) -> list[Article]:
    """Find articles relevant to a topic.

    Searches article titles, summaries, themes, and insights
    for the given topic string.

    Args:
        topic: The topic to search for.

    Returns:
        List of matching Articles, ordered by relevance (title match first).
    """
    if not topic or not isinstance(topic, str):
        return []

    topic_lower = topic.lower()
    scored: list[tuple[int, Article]] = []

    for article in ARTICLES:
        score = 0
        if topic_lower in article.title.lower():
            score += 3
        if any(topic_lower in t.lower() for t in article.themes):
            score += 2
        if topic_lower in article.summary.lower():
            score += 1
        if topic_lower in article.insight.lower():
            score += 1
        if score > 0:
            scored.append((score, article))

    scored.sort(key=lambda x: x[0], reverse=True)
    return [article for _, article in scored]
