import json
from pathlib import Path
from html import escape

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
CATEGORY_DIR = Path("category")

CATEGORY_DIR.mkdir(exist_ok=True)


class CategoryBuilder:

    def build(self):

        if not ARTICLES_FILE.exists():

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        grouped = {}

        for article in data.get("articles", []):

            category = article.get(
                "category",
                "General"
            )

            grouped.setdefault(
                category,
                []
            ).append(article)

        for category, articles in grouped.items():

            articles.sort(
                key=lambda x: x.get(
                    "published_at",
                    ""
                ),
                reverse=True
            )

            cards = ""

            for article in articles:

                cards += f"""
<article>

<h2>

<a href="../posts/{article['slug']}.html">

{escape(article['title'])}

</a>

</h2>

<p>

{escape(article['summary'])}

</p>

</article>
"""

            slug = (

                category.lower()

                .replace("&", "and")

                .replace(" ", "-")

            )

            html = f"""<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1">

<title>{escape(category)} | The Meridian Times</title>

<meta name="description"
content="Latest {escape(category)} news from The Meridian Times">

</head>

<body>

<header>

<h1>{escape(category)}</h1>

</header>

<main>

{cards}

</main>

</body>

</html>
"""

            (
                CATEGORY_DIR / f"{slug}.html"
            ).write_text(

                html,

                encoding="utf-8"

            )

        logger.info(

            f"Generated {len(grouped)} category pages."

        )


category_builder = CategoryBuilder()
