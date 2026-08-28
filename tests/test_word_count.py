import pytest

from textutils.word_count import word_count


def test_word_count_two_words():
    assert word_count("Hallo Welt") == 2


def test_word_count_irregular_whitespace():
    assert word_count("  a   b  c ") == 3


def test_word_count_empty_string():
    assert word_count("") == 0


def test_word_count_single_word():
    assert word_count("eins") == 1


def test_word_count_only_whitespace():
    assert word_count("   \t\n  ") == 0


def test_word_count_unicode():
    assert word_count("héllo wörld 世界 öäü") == 4


def test_word_count_emoji():
    assert word_count("Hallo 👋 Welt 🎉") == 4


def test_word_count_very_long_string():
    long_text = "wort " * 100000
    assert word_count(long_text) == 100000


@pytest.mark.parametrize(
    "text",
    [
        "",
        "   \n\t ",
        "Hallo Welt",
        "héllo wörld 世界",
        "👋 🎉",
        "x" * 1000000,
    ],
)
def test_word_count_no_unexpected_exceptions_for_valid_strings(text):
    assert isinstance(word_count(text), int)


@pytest.mark.parametrize("bad_input", [None, 42, 3.14, ["a", "b"], {"a": 1}])
def test_word_count_rejects_non_string_with_type_error(bad_input):
    with pytest.raises(TypeError):
        word_count(bad_input)
