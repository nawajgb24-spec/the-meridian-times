from core.database import database
from core.logger import logger


class InternalLinker:

    MAX_LINKS = 5

    def build(self, article):

        logger.info("=" * 60)
        logger.info("INTERNAL LINK ENGINE")
        logger.info("=" * 60)

        links = []

        current_slug = article.slug.lower()

        for existing in database.articles():

            slug = existing.get("slug", "").lower()

            if slug == current_slug:

                continue

            links.append({

                "title": existing.get("title", ""),

                "slug": existing.get("slug", ""),

                "category": existing.get("category", "")

            })

            if len(links) >= self.MAX_LINKS:

                break

        logger.info(

            f"Generated {len(links)} internal links."

        )

        logger.info("=" * 60)

        return links


internal_linker = InternalLinker()
