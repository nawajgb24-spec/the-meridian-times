from pathlib import Path
import json

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
SITEMAP_FILE = Path("sitemap.xml")


class SitemapBuilder:

    def build(self):

        if not ARTICLES_FILE.exists():

            return

        with open(

            ARTICLES_FILE,

            "r",

            encoding="utf-8"

        ) as f:

            data = json.load(f)

        xml = []

        xml.append('<?xml version="1.0" encoding="UTF-8"?>')

        xml.append(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
        )

        xml.append(
            """
<url>
<loc>https://themeridiantimes.com/</loc>
<priority>1.0</priority>
</url>
"""
        )

        for article in data.get("articles", []):

            xml.append(
                f"""
<url>

<loc>

https://themeridiantimes.com/posts/{article['slug']}.html

</loc>

<lastmod>

{article['published_at']}

</lastmod>

<priority>0.8</priority>

</url>
"""
            )

        xml.append("</urlset>")

        SITEMAP_FILE.write_text(

            "\n".join(xml),

            encoding="utf-8"

        )

        logger.info(

            "sitemap.xml generated."

        )


sitemap_builder = SitemapBuilder()
