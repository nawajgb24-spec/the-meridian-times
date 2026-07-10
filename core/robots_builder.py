from pathlib import Path

from core.logger import logger


ROBOTS_FILE = Path("robots.txt")


class RobotsBuilder:

    def build(self):

        content = """User-agent: *

Allow: /

Sitemap: https://themeridiantimes.com/sitemap.xml
"""

        ROBOTS_FILE.write_text(

            content,

            encoding="utf-8"

        )

        logger.info(

            "robots.txt generated."

        )


robots_builder = RobotsBuilder()
