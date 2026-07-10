from core.database import database
from core.logger import logger


class InternalLinker:

    MAX_LINKS = 5

    def build(self, article):

        logger.info("=" * 60)
        logger.info("SMART INTERNAL LINK ENGINE")
        logger.info("=" * 60)

        current_slug = article.slug.lower()

        article_keywords = {
            k.lower().strip()
            for k in article.keywords
            if k.strip()
        }

        scored = []

        for existing in database.articles():

            slug = existing.get("slug", "").lower()

            if slug == current_slug:
                continue

            existing_keywords = {
                k.lower().strip()
                for k in existing.get(
                    "keywords",
                    []
                )
                if k.strip()
            }

            score = len(
                article_keywords &
                existing_keywords
            )

            if (
                score == 0
                and existing.get(
                    "category",
                    ""
                ).lower()
                ==
                article.category.lower()
            ):
                score = 1

            if score > 0:

                scored.append(

                    (

                        score,

                        {

                            "title": existing.get(
                                "title",
                                ""
                            ),

                            "slug": existing.get(
                                "slug",
                                ""
                            ),

                            "category": existing.get(
                                "category",
                                ""
                            )

                        }

                    )

                )

        scored.sort(
            reverse=True,
            key=lambda x: x[0]
        )

        links = [

            item

            for _, item in scored[
                :self.MAX_LINKS
            ]

        ]

        logger.info(

            f"Generated {len(links)} ranked internal links."

        )

        logger.info("=" * 60)

        return links


internal_linker = InternalLinker()
