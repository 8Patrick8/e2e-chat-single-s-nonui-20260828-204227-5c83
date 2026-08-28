import string

import pytest

from textutils.slugify import slugify

AC08_ALLOWED = set(string.ascii_lowercase + string.digits + "-")


def test_hello_world():
    assert slugify("Hello, World!") == "hello-world"


def test_surrounding_hyphens_and_whitespace():
    assert slugify("  --Foo--  ") == "foo"


def test_empty_string():
    assert slugify("") == ""


def test_lowercases_input():
    assert slugify("HELLO WORLD") == "hello-world"


def test_consecutive_hyphens_are_collapsed():
    assert slugify("foo--bar") == "foo-bar"
    assert slugify("foo --- bar") == "foo-bar"


def test_runs_of_non_alphanumerics_become_single_hyphen():
    assert slugify("Hello,   World!!!") == "hello-world"


def test_leading_and_trailing_hyphens_are_removed():
    assert slugify("--foo--") == "foo"
    assert slugify("-") == ""


def test_preserves_ascii_letters_and_digits():
    assert slugify("abc123") == "abc123"


@pytest.mark.parametrize(
    "text",
    [
        "Héllo Wörld",
        "Grüße",
        "日本語テキスト",
        "👍 emoji",
        "café_olé",
        "Σωκράτης",
        "Straße 123",
        "üäöß",
    ],
)
def test_non_ascii_is_replaced_or_removed(text):
    slug = slugify(text)
    assert set(slug) <= AC08_ALLOWED


@pytest.mark.parametrize(
    "text",
    [
        "  ",
        "\t\n\r",
        "   \t  ",
        "ü",
        "👍",
        "---",
        "_",
        "!!!",
    ],
)
def test_whitespace_and_non_ascii_only_returns_empty(text):
    assert slugify(text) == ""


def test_very_long_string_does_not_raise():
    unit = "  Hello, Wörld!  "
    long_text = unit * 20000
    slug = slugify(long_text)
    assert slug == "-".join(["hello-w-rld"] * 20000)
    assert len(slug) < len(long_text)


def test_type_error_for_non_str():
    for bad in (None, 123, 3.14, b"bytes", ["list"], {"a": 1}):
        with pytest.raises(TypeError):
            slugify(bad)  # type: ignore[arg-type]
