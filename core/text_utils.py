import re


def word_count(text: str) -> int:
    return len(text.split())


def reading_time(text: str) -> int:
    words = word_count(text)
    return max(1, round(words / 200))


def clean_text(text: str) -> str:

    text = re.sub(r"\r\n", "\n", text)

    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()
