# textutils

Kleine Python-String-Bibliothek mit fünf unabhängigen, reinen String-Hilfsfunktionen:
`slugify`, `truncate`, `word_count`, `is_palindrome` und `reverse_words`.
Reines Backend, keine UI und kein HTTP-Server — das Paket wird als Bibliothek importiert.

## Tech-Stack

- **Sprache**: Python 3
- **Laufzeit**: nur Standardbibliothek, keine Drittanbieter-Abhängigkeiten
- **Tests**: pytest

## Installation

Das Paket liegt direkt an der Wurzel des Repositories; eine Installation über einen
Paketmanager ist nicht nötig. Für die Tests wird pytest benötigt:

```bash
py -m pip install pytest
```

## Ausführung

Es gibt keinen Server und kein UI — das Produkt ist eine importierbare Bibliothek:

```python
from textutils import slugify, truncate, word_count, is_palindrome, reverse_words
```

## Tests

Die Testsuite wird mit pytest ausgeführt:

```bash
pytest
```

## Öffentliche API

Alle fünf Funktionen sind über `from textutils import ...` importierbar und werden
aus ihren jeweiligen Einzelmodulen re-exportiert:

| Funktion | Signatur | Beschreibung |
| --- | --- | --- |
| `slugify` | `slugify(text: str) -> str` | Erzeugt aus einem String einen URL-/Dateinamen-freundlichen Slug aus ASCII-Zeichen `[a-z0-9-]`. |
| `truncate` | `truncate(text: str, max_len: int) -> str` | Kürzt einen String auf höchstens `max_len` Zeichen und endet bei Kürzung mit `…`. |
| `word_count` | `word_count(text: str) -> int` | Zählt die Wörter im String (getrennt durch Whitespace). |
| `is_palindrome` | `is_palindrome(text: str) -> bool` | Prüft, ob der String (ignoriert Groß-/Kleinschreibung, Leerraum und Satzzeichen) ein Palindrom ist. |
| `reverse_words` | `reverse_words(text: str) -> str` | Kehrt die Reihenfolge der Wörter im String um. |

> **Hinweis**: Die Funktionen sind derzeit Stubs mit vollständiger Signatur und werfen
> `NotImplementedError`. Die Implementierungen folgen mit den Feature-Tickets; die
> Signaturen bleiben unverändert.

## Features

- `slugify`: String → Slug aus `[a-z0-9-]`
- `truncate`: String auf maximale Länge kürzen
- `word_count`: Wortanzahl eines Strings
- `is_palindrome`: Palindrom-Prüfung
- `reverse_words`: Wortreihenfolge umkehren
