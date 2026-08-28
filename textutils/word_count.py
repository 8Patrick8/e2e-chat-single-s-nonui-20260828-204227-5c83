def word_count(text: str) -> int:
    """Return the number of words in ``text``.

    Words are separated by arbitrary whitespace sequences (``text.split()``).
    An empty string yields ``0``.
    """
    return len(text.split())
