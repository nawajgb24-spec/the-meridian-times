
import json
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path
from xml.sax.saxutils import escape

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
RSS_FILE = Path("rss.xml")

SITE_URL = "https://themeridiantimes.com"


class RSSBuilder:

    MAX_ITEMS = 50

    def build(self):

        if not ARTICLES_FILE.exists():

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
        )[:self.MAX_ITEMS]

        now = format_datetime(
            datetime.now(timezone.utc)
        )

        xml = []

        xml.append('<?xml version="1.0" encoding="UTF-8"?>')
        xml.append('<rss version="2.0">')
        xml.append("<channel>")

        xml.append("<title>The Meridian Times</title>")
        xml.append(f"<link>{SITE_URL}</link>")
        xml.append(
            "<description>Latest global news from The Meridian Times</description>"
        )
        xml.append("<language>en-US</language>")
        xml.append(f"<lastBuildDate>{now}</lastBuildDate>")
        xml.append("<generator>The Meridian Times AI Engine</generator>")

        for article in articles:

            try:

                published = datetime.fromisoformat(
                    article["published_at"]
                )

                if published.tzinfo is None:

                    published = published.replace(
                        tzinfo=timezone.utc
                    )

                pub_date = format_datetime(
                    published
                )

            except Exception:

                pub_date = article.get(
                    "published_at",
                    ""
                )

            url = (
                f"{SITE_URL}/posts/{article['slug']}.html"
            )

            xml.append("<item>")

            xml.append(
                f"<title>{escape(article['title'])}</title>"
            )

            xml.append(
                f"<link>{url}</link>"
            )

            xml.append(
                f"<guid isPermaLink=\"true\">{url}</guid>"
            )

            xml.append(
                f"<description>{escape(article['summary'])}</description>"
            )

            xml.append(
                f"<pubDate>{pub_date}</pubDate>"
            )

            xml.append("</item>")

        xml.append("</channel>")
        xml.append("</rss>")

        RSS_FILE.write_text(
            "\n".join(xml),
            encoding="utf-8"
        )

        logger.info(
            "rss.xml generated."
        )


rss_builder = RSSBuilder()
