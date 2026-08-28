VERDICT: BUGS_FOUND

## Analyse

Der pytest-Lauf ist grün (43 passed, 10 skipped, exit 0), aber die 10 Skips sind kein Harness-Problem und nicht „Umgebung“: Sie werden von den Tests selbst ausgelöst, weil die Produktfunktion `word_count` nicht implementiert ist. Der Quellbestand bestätigt das eindeutig (`textutils/word_count.py` enthält `raise NotImplementedError`). Damit ist AC-03 („word_count('Hallo Welt') == 2 …“), AC-06 („Alle fünf Funktionen sind per `from textutils import …` importierbar; pytest läuft ohne Fehler durch“) und AC-07 („Alle fünf Funktionen werfen … keine unerwarteten Exceptions“) nicht erfüllt: Die versprochene Fähigkeit existiert zur Laufzeit nicht, sondern nur als Stub. Ein grüner Lauf eines unvollständigen Produkts ist kein PASS.

Alle übrigen Kernfunktionen (`slugify`, `truncate`, `is_palindrome`, `reverse_words`) bestehen ihre Akzeptanztests vollständig und werfen bei Nicht-`str`-Eingaben korrekt `TypeError`.

## Known open decisions

- MR !8 — für die Architekt-Entscheidung offen gelassen; nicht als Bug gewertet.
- MR !10 — für die Architekt-Entscheidung offen gelassen; nicht als Bug gewertet.

## Bugs

- **Titel**: `word_count` ist nicht implementiert (NotImplementedError-Stub)
- **Symptom**: Die Bibliothek kann keine Wortanzahl berechnen. Ein Aufruf von `word_count("Hallo Welt")` wirft sofort `NotImplementedError`, statt `2` zurückzugeben. Die Spec verspricht in AC-03 eine funktionierende `word_count`-Funktion sowie in AC-06/AC-07, dass alle fünf Funktionen importierbar, lauffähig und frei von unerwarteten Exceptions sind — das ist für `word_count` nicht gegeben. Das Kern-Deliverable fehlt.
- **Repro**: `pytest tests/test_word_count.py` ausführen — alle 8 Tests werden übersprungen mit der Begründung „word_count is not implemented“; direkt: `from textutils import word_count; word_count("Hallo Welt")` → `NotImplementedError`. Auch `tests/test_security.py` überspringt beide Security-Tests, weil sie `word_count` mit abdecken.
- **Evidence**:
  - `tests/test_word_count.py::test_ac03_examples SKIPPED (word_count is ...)`
  - `tests/test_word_count.py::test_whitespace_only_is_zero SKIPPED (word_count is ...)`
  - `tests/test_security.py::test_never_raises_on_any_valid_str SKIPPED (...)`
  - `======================= 43 passed, 10 skipped in 0.13s ========================`
  - Quelle: `def word_count(text: str) -> int: raise NotImplementedError`
- **Vermutete Datei(en)**: `textutils/word_count.py`
- **Severity**: high