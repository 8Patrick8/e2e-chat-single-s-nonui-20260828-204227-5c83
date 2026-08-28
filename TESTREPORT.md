VERDICT: BUGS_FOUND

## Strukturierte Bugliste

- **Titel**: `truncate` ist nicht implementiert — Kernfunktion der Bibliothek fehlt
- **Symptom**: Die Spec (AC-02) verlangt, dass `truncate('Hallo Welt', 5)` mit `…` endet und insgesamt `max_len` Zeichen hat; `truncate('kurz', 10) == 'kurz'`; `truncate('x', 0) == ''`. Stattdessen wirft die Funktion zur Laufzeit `NotImplementedError`. Sämtliche Tests, die dieses Verhalten prüfen würden, sind übersprungen, sodass der pytest-Lauf grün erscheint, obwohl die geforderte Fähigkeit nie existiert.
- **Repro**: `from textutils import truncate; truncate('Hallo Welt', 5)` → `NotImplementedError`; im Testlauf: `tests/test_truncate.py::test_ac02_examples SKIPPED (truncate is not ...)`.
- **Evidence**: `tests/test_truncate.py::test_ac02_examples SKIPPED (truncate is not ...)` — sowie alle weiteren 9 truncate-Tests SKIPPED; die Quelldatei enthält `raise NotImplementedError`.
- **Suspected file(s)**: `textutils/truncate.py`
- **Severity**: high (AC-02-Deliverable fehlt; grüne Suite nur durch Überspringen der Tests)

---

- **Titel**: `word_count` ist nicht implementiert — Kernfunktion der Bibliothek fehlt
- **Symptom**: Die Spec (AC-03) verlangt `word_count('Hallo Welt') == 2`, `word_count('  a   b  c ') == 3`, `word_count('') == 0`. Stattdessen wirft die Funktion zur Laufzeit `NotImplementedError`. Alle Tests für diese Funktion sind übersprungen; der grüne pytest-Exit kaschiert, dass die geforderte Fähigkeit nicht existiert.
- **Repro**: `from textutils import word_count; word_count('Hallo Welt')` → `NotImplementedError`; im Testlauf: `tests/test_word_count.py::test_ac03_examples SKIPPED (word_count is ...)`.
- **Evidence**: `tests/test_word_count.py::test_ac03_examples SKIPPED (word_count is ...)` — sowie alle weiteren 8 word_count-Tests SKIPPED; die Quelldatei enthält `raise NotImplementedError`.
- **Suspected file(s)**: `textutils/word_count.py`
- **Severity**: high (AC-03-Deliverable fehlt; grüne Suite nur durch Überspringen der Tests)

---

## Known open decisions

- **MR !8** — vom Architekten auf dem Demo zu entscheiden; nicht als Bug gewertet. Code kann auf main liegen (Stacked Ticket).
- **MR !10** — vom Architekten auf dem Demo zu entscheiden; nicht als Bug gewertet. Code kann auf main liegen (Stacked Ticket).

## Zusammenfassung

Der Testlauf ist formal grün (34 passed, Exit 0), aber er beweist nicht das laut Spec geforderte Produkt: Zwei der fünf versprochenen Kernfunktionen (`truncate`, `word_count`) werfen `NotImplementedError`, und genau ihre Tests sind per pytest-Skip ausgeblendet. Das ist kein Umgebungs- oder Harness-Problem — die `SKIPPED`-Markierungen sind durch den `NotImplementedError`-Produktzustand verursacht, nicht durch die Unfähigkeit des Runners. AC-02 und AC-03 sind damit nicht erfüllt, und AC-06 („pytest läuft ohne Fehler durch") ist nur erfüllt, weil die Suite die defekten Funktionen nicht prüft. Die Funktionalität der übrigen drei Funktionen (slugify, is_palindrome, reverse_words) wird durch die grünen Tests hinreichend belegt.