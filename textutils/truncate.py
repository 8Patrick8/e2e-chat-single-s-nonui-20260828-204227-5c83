def truncate(text: str, max_len: int) -> str:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    if max_len <= 0:
        return ""
    if len(text) <= max_len:
        return text
    return text[: max_len - 1] + "…"
