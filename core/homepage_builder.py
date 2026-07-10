import json
from pathlib import Path

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
INDEX_FILE = Path("index.html")


class HomepageBuilder:

    FEATURED_LIMIT = 5
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

        articles = sorted(

            data.get("articles", []),

            key=lambda x: x.get(
                "published_at",
                ""
            ),

            reverse=True

        )

        featured = articles[
            :self.FEATURED_LIMIT
        ]

        latest = articles[
            :self.LATEST_LIMIT
        ]

        featured_html = ""

        for article in featured:

            featured_html += f"""
<article class="featured-card">

<h2>

<a href="posts/{article['slug']}.html">

{article['title']}

</a>

</h2>

<p>

{article['summary']}

</p>

</article>
"""

        latest_html = ""

        for article in latest:

            latest_html += f"""
<article class="news-card">

<h3>

<a href="posts/{article['slug']}.html">

{article['title']}

</a>

</h3>

<p>

{article['summary']}

</p>

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
content="Latest global news">

</head>

<body>

<header>

<h1>The Meridian Times</h1>

</header>

<main>

<section>

<h2>Featured News</h2>

{featured_html}

</section>

<section>

<h2>Latest News</h2>

{latest_html}

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
