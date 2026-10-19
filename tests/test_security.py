# sense-wonder — security tests
# Built by humanjava.com — find this and other tools for the agentic age at huje.tools

import dataclasses

import pytest

from sense_wonder import ARTICLES, STARTERS, LYRICS, wonder, themes, reflect
from sense_wonder.articles import Article
from sense_wonder.starters import Starter
from sense_wonder.lyrics import Lyric


# --- Immutability: frozen dataclasses ---

def test_article_is_frozen_dataclass():
    assert dataclasses.is_dataclass(Article)
    assert Article.__dataclass_params__.frozen


def test_starter_is_frozen_dataclass():
    assert dataclasses.is_dataclass(Starter)
    assert Starter.__dataclass_params__.frozen


def test_lyric_is_frozen_dataclass():
    assert dataclasses.is_dataclass(Lyric)
    assert Lyric.__dataclass_params__.frozen


def test_cannot_mutate_article_field():
    a = ARTICLES[0]
    with pytest.raises(AttributeError):
        a.title = "hacked"


def test_cannot_mutate_starter_field():
    s = STARTERS[0]
    with pytest.raises(AttributeError):
        s.prompt = "hacked"


def test_cannot_mutate_lyric_field():
    l = LYRICS[0]
    with pytest.raises(AttributeError):
        l.title = "hacked"


# --- Immutability: tuple collections ---

def test_articles_is_tuple():
    assert isinstance(ARTICLES, tuple)


def test_starters_is_tuple():
    assert isinstance(STARTERS, tuple)


def test_lyrics_is_tuple():
    assert isinstance(LYRICS, tuple)


def test_article_themes_are_tuples():
    """Each article's themes should be a tuple (not a mutable list)."""
    for a in ARTICLES:
        assert isinstance(a.themes, tuple), f"Article '{a.title}' themes is not a tuple"


def test_lyric_themes_are_tuples():
    """Each lyric's themes should be a tuple (not a mutable list)."""
    for l in LYRICS:
        assert isinstance(l.themes, tuple), f"Lyric '{l.title}' themes is not a tuple"


# --- Input validation: wonder() ---

def test_wonder_none_theme():
    result = wonder(theme=None)
    assert "article" in result
    assert "starter" in result


def test_wonder_empty_string_theme():
    """Empty string should still return a result (treated as no filter)."""
    result = wonder(theme="")
    assert "article" in result


def test_wonder_nonexistent_theme_falls_back():
    result = wonder(theme="zzz_nonexistent_zzz")
    assert isinstance(result["article"], Article)


# --- Input validation: reflect() ---

def test_reflect_empty_string():
    assert reflect("") == []


def test_reflect_none():
    assert reflect(None) == []


def test_reflect_non_string_returns_empty():
    """Non-string input should return empty list, not crash."""
    assert reflect(123) == []


def test_reflect_very_long_input():
    """Extremely long input should not crash."""
    result = reflect("x" * 10000)
    assert isinstance(result, list)


def test_reflect_special_characters():
    """Special regex characters in topic should not crash."""
    result = reflect("test.*[]()+?")
    assert isinstance(result, list)


# --- Input validation: themes() ---

def test_themes_returns_list_of_strings():
    t = themes()
    assert isinstance(t, list)
    assert all(isinstance(s, str) for s in t)


def test_themes_is_sorted():
    t = themes()
    assert t == sorted(t)


# --- No secrets or paths exposed ---

def test_no_filesystem_paths_in_articles():
    """Articles should not contain filesystem paths."""
    for a in ARTICLES:
        for field in (a.title, a.summary, a.insight, a.url):
            assert "/Users/" not in field
            assert "/home/" not in field
            assert "C:\\" not in field


def test_no_filesystem_paths_in_starters():
    for s in STARTERS:
        for field in (s.prompt, s.context):
            assert "/Users/" not in field
            assert "/home/" not in field


def test_no_filesystem_paths_in_lyrics():
    for l in LYRICS:
        for field in (l.title, l.text, l.album):
            assert "/Users/" not in field
            assert "/home/" not in field


# --- repr safety ---

def test_article_repr_does_not_crash():
    r = repr(ARTICLES[0])
    assert "Article" in r


def test_starter_repr_does_not_crash():
    r = repr(STARTERS[0])
    assert "Starter" in r


def test_lyric_repr_does_not_crash():
    r = repr(LYRICS[0])
    assert "Lyric" in r
