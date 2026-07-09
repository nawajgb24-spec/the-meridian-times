import json
from pathlib import Path

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
INDEX_FILE = Path("index.html")


class HomepageBuilder:

    def build(self):

        if not ARTICLES_FILE.exists():

            logger.warning("articles.json not found.")

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        articles = data.get("articles", [])

        articles = sorted(

            articles,

            key=lambda x: x["published_at"],

            reverse=True

        )[:30]

        cards = ""

        for article in articles:

            cards += f"""
<article class="news-card">

<h2>
<a href="posts/{article['slug']}.html">
{article['title']}
</a>
</h2>

<p>{article['summary']}</p>

<small>

{article['category']}

</small>

</article>

"""

        html = f"""<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1">

<title>The Meridian Times</title>

<meta name="description"
content="Latest News">

</head>

<body>

<header>

<h1>The Meridian Times</h1>

</header>

<main>

{cards}

</main>

</body>

</html>
"""

        INDEX_FILE.write_text(

            html,

            encoding="utf-8"

        )

        logger.info("Homepage generated.")


homepage_builder = HomepageBuilder()
