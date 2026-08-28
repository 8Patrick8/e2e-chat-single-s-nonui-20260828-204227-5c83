import inspect

from textutils import is_palindrome, reverse_words, slugify, truncate, word_count

ALL_FUNCTIONS = (slugify, truncate, word_count, is_palindrome, reverse_words)

EXPECTED_SIGNATURES = {
    "slugify": "(text: str) -> str",
    "truncate": "(text: str, max_len: int) -> str",
    "word_count": "(text: str) -> int",
    "is_palindrome": "(text: str) -> bool",
    "reverse_words": "(text: str) -> str",
}


def test_all_five_functions_are_importable_and_callable():
    for func in ALL_FUNCTIONS:
        assert callable(func)


def test_functions_are_reexported_from_their_own_modules():
    for func in ALL_FUNCTIONS:
        assert func.__module__.startswith("textutils.")


def test_functions_expose_the_binding_signatures():
    for func in ALL_FUNCTIONS:
        assert str(inspect.signature(func)) == EXPECTED_SIGNATURES[func.__name__]
