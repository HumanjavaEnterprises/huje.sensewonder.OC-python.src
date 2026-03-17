"""Tests for sense-wonder."""

from sense_wonder import ARTICLES, STARTERS, LYRICS, wonder, themes, reflect
from sense_wonder.articles import Article
from sense_wonder.starters import Starter
from sense_wonder.lyrics import Lyric


def test_articles_exist():
    assert len(ARTICLES) == 14


def test_starters_exist():
    assert len(STARTERS) == 34


def test_articles_are_frozen():
    a = ARTICLES[0]
    assert isinstance(a, Article)
    try:
        a.title = "changed"
        assert False, "Should not be mutable"
    except AttributeError:
        pass


def test_starters_are_frozen():
    s = STARTERS[0]
    assert isinstance(s, Starter)
    try:
        s.prompt = "changed"
        assert False, "Should not be mutable"
    except AttributeError:
        pass


def test_all_articles_have_fields():
    for a in ARTICLES:
        assert a.title
        assert a.url.startswith("https://")
        assert a.summary
        assert len(a.themes) >= 3
        assert a.insight


def test_all_starters_have_fields():
    for s in STARTERS:
        assert s.prompt
        assert s.context


def test_wonder_returns_article_and_starter():
    result = wonder()
    assert "article" in result
    assert "starter" in result
    assert isinstance(result["article"], Article)
    assert isinstance(result["starter"], Starter)


def test_wonder_with_theme():
    result = wonder(theme="consciousness")
    assert isinstance(result["article"], Article)


def test_wonder_with_unknown_theme_falls_back():
    result = wonder(theme="xyznonexistent")
    assert isinstance(result["article"], Article)


def test_themes_returns_sorted_list():
    t = themes()
    assert isinstance(t, list)
    assert len(t) > 20
    assert t == sorted(t)


def test_reflect_finds_articles():
    results = reflect("consciousness")
    assert len(results) > 0
    assert all(isinstance(a, Article) for a in results)


def test_reflect_ranks_title_match_higher():
    results = reflect("scarcity")
    assert len(results) >= 2
    # "Beyond Scarcity" should rank higher than articles that just mention it
    assert "Scarcity" in results[0].title


def test_reflect_empty_topic():
    assert reflect("") == []
    assert reflect(None) == []


def test_no_duplicate_starters():
    prompts = [s.prompt for s in STARTERS]
    assert len(prompts) == len(set(prompts))


def test_no_duplicate_articles():
    urls = [a.url for a in ARTICLES]
    assert len(urls) == len(set(urls))


def test_lyrics_exist():
    assert len(LYRICS) == 16


def test_lyrics_are_frozen():
    l = LYRICS[0]
    assert isinstance(l, Lyric)
    try:
        l.title = "changed"
        assert False, "Should not be mutable"
    except AttributeError:
        pass


def test_all_lyrics_have_fields():
    for l in LYRICS:
        assert l.title
        assert l.album
        assert len(l.themes) >= 2
        assert l.text


def test_lyrics_albums():
    albums = {l.album for l in LYRICS}
    assert "Resonance" in albums
    assert "Recognition" in albums
    assert "Don't Miss" in albums
    assert "Duality" in albums


def test_no_duplicate_lyrics():
    titles = [(l.title, l.album) for l in LYRICS]
    assert len(titles) == len(set(titles))
