import json
from pathlib import Path

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
INDEX_FILE = Path("index.html")


class HomepageBuilder:

    FEATURED_LIMIT = 5
    TRENDING_LIMIT = 10
    LATEST_LIMIT = 30

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

        latest = sorted(
            articles,
            key=lambda x: x.get(
                "published_at",
                ""
            ),
            reverse=True
        )

        trending = sorted(
            articles,
            key=lambda x: x.get(
                "trending_score",
                0
            ),
            reverse=True
        )

        featured = trending[:self.FEATURED_LIMIT]
        trending = trending[:self.TRENDING_LIMIT]
        latest = latest[:self.LATEST_LIMIT]

        def render(items, heading_level):

            html = ""

            for article in items:

                html += f"""
<article class="news-card">

<h{heading_level}>
<a href="posts/{article['slug']}.html">
{article['title']}
</a>
</h{heading_level}>

<p>{article['summary']}</p>

<small>
{article['category']}
</small>

</article>
"""

            return html

        html = f"""<!DOCTYPE html>

<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1">

<title>The Meridian Times</title>

<meta name="description"
content="Latest global news">

</head>

<body>

<header>

<h1>The Meridian Times</h1>

</header>

<main>

<section>

<h2>⭐ Featured Stories</h2>

{render(featured, 2)}

</section>

<section>

<h2>🔥 Trending News</h2>

{render(trending, 3)}

</section>

<section>

<h2>📰 Latest News</h2>

{render(latest, 3)}

</section>

</main>

</body>

</html>
"""

        INDEX_FILE.write_text(

            html,

            encoding="utf-8"

        )

        logger.info(
            "Homepage generated."
        )


homepage_builder = HomepageBuilder()
