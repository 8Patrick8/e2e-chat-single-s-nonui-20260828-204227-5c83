from textutils.is_palindrome import is_palindrome


def test_classic_palindromes():
    assert is_palindrome("Anna")
    assert is_palindrome("A man, a plan, a canal: Panama")


def test_non_palindrome():
    assert not is_palindrome("Hallo")


def test_case_insensitive():
    assert is_palindrome("aNnA")


def test_punctuation_and_spaces_ignored():
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("Never odd or even")
    assert is_palindrome("Step on no pets")


def test_digits_are_kept():
    assert is_palindrome("12321")
    assert is_palindrome("1, 2, 3, 2, 1")
    assert not is_palindrome("12345")


def test_empty_string_is_palindrome():
    assert is_palindrome("")


def test_only_whitespace_is_palindrome():
    assert is_palindrome("   \t\n  ")


def test_only_punctuation_is_palindrome():
    assert is_palindrome(".,!?;:")


def test_single_character_is_palindrome():
    assert is_palindrome("a")


def test_unicode_palindrome():
    assert is_palindrome("Été")
    assert is_palindrome("Madam, I'm Adam")


def test_emoji_is_ignored():
    assert is_palindrome("🙂 Anna 🙂")
    assert is_palindrome("A🙂B🙂B🙂A")


def test_very_long_string():
    text = "a" * 100_000
    assert is_palindrome(text)
    text = "a" * 99_999 + "b"
    assert not is_palindrome(text)


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
        is_palindrome(text)


def test_type_error_for_non_str():
    for bad in (None, 42, 3.14, ["a", "b"], {"a": 1}, b"bytes", True):
        try:
            is_palindrome(bad)
        except TypeError:
            continue
        raise AssertionError(f"is_palindrome({bad!r}) did not raise TypeError")
