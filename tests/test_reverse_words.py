from textutils.reverse_words import reverse_words


def test_reverse_sentence():
    assert reverse_words("Hallo Welt Test") == "Test Welt Hallo"


def test_empty_string():
    assert reverse_words("") == ""


def test_only_whitespace():
    assert reverse_words("   \t\n  ") == ""


def test_whitespace_is_normalized():
    assert reverse_words("  a   b  c ") == "c b a"


def test_single_word_stays_unchanged():
    assert reverse_words("Hallo") == "Hallo"


def test_words_themselves_are_not_reversed():
    assert reverse_words("Hello World") == "World Hello"
    assert reverse_words("Hello World").split() == ["World", "Hello"]


def test_unicode_words():
    assert reverse_words("Grüße 世界") == "世界 Grüße"


def test_emoji_words():
    assert reverse_words("😀 🎉 hallo") == "hallo 🎉 😀"


def test_very_long_string():
    text = " ".join(f"word{i}" for i in range(100_000))
    result = reverse_words(text)
    assert result == " ".join(f"word{i}" for i in range(99_999, -1, -1))


def test_mixed_unicode_and_emoji_never_raises():
    inputs = [
        "",
        "   ",
        "äöü ß éèê",
        "🙂 🚀 中文 العربية",
        "a" * 10_000,
        " ".join(["🙂" * 10] * 1000),
    ]
    for text in inputs:
        reverse_words(text)


def test_type_error_for_non_str():
    for bad in (None, 42, 3.14, ["a", "b"], {"a": 1}, b"bytes", True):
        try:
            reverse_words(bad)
        except TypeError:
            continue
        raise AssertionError(f"reverse_words({bad!r}) did not raise TypeError")
