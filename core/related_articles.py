from core.database import database
from core.logger import logger


class RelatedArticles:

    MAX_RELATED = 5

    def find(self, article):

        logger.info("=" * 60)
        logger.info("RELATED ARTICLES ENGINE")
        logger.info("=" * 60)

        category = article.category.lower()

        related = []

        for existing in database.articles():

            if existing.get("slug") == article.slug:
                continue

            if existing.get(
                "category",
                ""
            ).lower() != category:
                continue

            related.append({

                "title": existing.get("title", ""),

                "slug": existing.get("slug", ""),

                "summary": existing.get("summary", "")

            })

            if len(related) >= self.MAX_RELATED:
                break

        logger.info(
            f"Found {len(related)} related articles."
        )

        logger.info("=" * 60)

        return related


related_articles = RelatedArticles()
