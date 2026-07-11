from pathlib import Path

from core.logger import logger


ROBOTS_FILE = Path("robots.txt")

SITE_URL = "https://themeridiantimes.com"


class RobotsBuilder:

    def build(self):

        content = f"""User-agent: *

Allow: /

Sitemap: {SITE_URL}/sitemap.xml
Sitemap: {SITE_URL}/news-sitemap.xml
Sitemap: {SITE_URL}/rss.xml
"""

        ROBOTS_FILE.write_text(

            content,

            encoding="utf-8"

        )

        logger.info(

            "robots.txt generated."

        )


robots_builder = RobotsBuilder()
