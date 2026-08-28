def word_count(text: str) -> int:
    """Return the number of words in ``text``.

    Words are separated by arbitrary whitespace sequences (``text.split()``).
    An empty string yields ``0``.
    """
    if not isinstance(text, str):
        raise TypeError(f"word_count() expects str, got {type(text).__name__}")
    return len(text.split())
