def is_palindrome(text: str) -> bool:
    if not isinstance(text, str):
        raise TypeError("text must be a str")
    letters = [char.lower() for char in text if char.isalnum()]
    return letters == letters[::-1]
