"""textutils — kleine Python-String-Bibliothek.

Re-exportiert alle fünf öffentlichen String-Hilfsfunktionen aus ihren
Einzelmodulen, sodass sie per ``from textutils import ...`` erreichbar sind.
"""

from textutils.is_palindrome import is_palindrome
from textutils.reverse_words import reverse_words
from textutils.slugify import slugify
from textutils.truncate import truncate
from textutils.word_count import word_count

__all__ = [
    "is_palindrome",
    "reverse_words",
    "slugify",
    "truncate",
    "word_count",
]
