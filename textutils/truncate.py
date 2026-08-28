"""Kürzt Text auf maximal max_len Zeichen.

Bei einer Kürzung endet das Ergebnis mit einem Auslassungszeichen '…'
(U+2026), das in max_len eingerechnet wird.
"""


def truncate(text: str, max_len: int) -> str:
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"
