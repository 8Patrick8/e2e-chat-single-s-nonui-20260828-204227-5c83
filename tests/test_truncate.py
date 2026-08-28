import pytest

from textutils import truncate


def test_truncate_long_text_ends_with_ellipsis_and_has_exact_length():
    result = truncate("Hallo Welt", 5)
    assert result == "Hall…"
    assert result.endswith("…")
    assert len(result) == 5


def test_truncate_short_text_returned_unchanged():
    assert truncate("kurz", 10) == "kurz"


def test_truncate_zero_max_len_returns_empty_string():
    assert truncate("x", 0) == ""


def test_truncate_negative_max_len_returns_empty_string():
    assert truncate("Hallo Welt", -1) == ""
    assert truncate("", -5) == ""


def test_truncate_text_exactly_max_len_returned_unchanged():
    assert truncate("Hallo", 5) == "Hallo"
    assert truncate("kurz", 4) == "kurz"


def test_truncate_max_len_one_yields_only_ellipsis():
    assert truncate("abc", 1) == "…"


def test_truncate_never_exceeds_max_len():
    for max_len in range(1, 10):
        result = truncate("Hallo Welt mit sehr langem Text", max_len)
        assert len(result) == max_len


def test_truncate_empty_string_does_not_raise():
    assert truncate("", 5) == ""
    assert truncate("", 0) == ""


def test_truncate_whitespace_only_does_not_raise():
    result = truncate("   \t\n  ", 2)
    assert len(result) == 2
    assert result.endswith("…")
    assert truncate("   ", 3) == "   "


def test_truncate_unicode_does_not_raise():
    result = truncate("Grüße aus Köln", 6)
    assert len(result) == 6
    assert result.endswith("…")


def test_truncate_emoji_does_not_raise():
    result = truncate("😀😀😀😀😀", 3)
    assert len(result) == 3
    assert result.endswith("…")


def test_truncate_very_long_string_does_not_raise():
    result = truncate("a" * 10_000, 42)
    assert len(result) == 42
    assert result.endswith("…")


def test_truncate_non_str_raises_typeerror():
    with pytest.raises(TypeError):
        truncate(123, 5)
