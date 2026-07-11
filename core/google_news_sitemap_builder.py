import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from xml.sax.saxutils import escape

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
NEWS_SITEMAP_FILE = Path("news-sitemap.xml")

SITE_URL = "https://themeridiantimes.com"


class GoogleNewsSitemapBuilder:

    def build(self):

        if not ARTICLES_FILE.exists():

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        cutoff = datetime.now(
            timezone.utc
        ) - timedelta(days=2)

        xml = []

        xml.append(
            '<?xml version="1.0" encoding="UTF-8"?>'
        )

        xml.append(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:news="http://www.google.com/schemas/sitemap-news/0.9">'
        )

        for article in data.get(
            "articles",
            []
        ):

            try:

                published = datetime.fromisoformat(
                    article["published_at"]
                )

                if published.tzinfo is None:

                    published = published.replace(
                        tzinfo=timezone.utc
                    )

            except Exception:

                continue

            if published < cutoff:

                continue

            xml.append(f"""
<url>

<loc>{SITE_URL}/posts/{article['slug']}.html</loc>

<news:news>

<news:publication>

<news:name>The Meridian Times</news:name>

<news:language>en</news:language>

</news:publication>

<news:publication_date>

{published.isoformat()}

</news:publication_date>

<news:title>

{escape(article['title'])}

</news:title>

</news:news>

</url>
""")

        xml.append("</urlset>")

        NEWS_SITEMAP_FILE.write_text(

            "\n".join(xml),

            encoding="utf-8"

        )

        logger.info(

            "news-sitemap.xml generated."

        )


google_news_sitemap_builder = GoogleNewsSitemapBuilder()
