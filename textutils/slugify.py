import re


def slugify(text: str) -> str:
    if not isinstance(text, str):
        raise TypeError(f"slugify() expects str, got {type(text).__name__}")
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")
