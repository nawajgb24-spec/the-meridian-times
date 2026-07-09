import re
from datetime import datetime


def slugify(text: str) -> str:

    slug = re.sub(
        r"[^a-zA-Z0-9]+",
        "-",
        text.lower()
    )

    slug = slug.strip("-")

    return slug


def word_count(text: str) -> int:

    return len(re.findall(r"\w+", text))


def reading_time(words: int) -> int:

    minutes = round(words / 200)

    return max(1, minutes)


def utc_now() -> str:

    return datetime.utcnow().isoformat()
