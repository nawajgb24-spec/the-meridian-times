from core.logger import logger


class FactChecker:

    REQUIRED_FIELDS = (

        "title",

        "summary",

        "content",

        "seo_title",

        "seo_description",

    )

    def validate(self, article):

        logger.info("=" * 60)
        logger.info("FACT CHECK")
        logger.info("=" * 60)

        for field in self.REQUIRED_FIELDS:

            value = getattr(article, field, "")

            if not str(value).strip():

                raise ValueError(

                    f"{field} missing."

                )

        if len(article.content.split()) < 900:

            raise ValueError(

                "Content below minimum length."

            )

        logger.info("Fact Check Passed")

        logger.info("=" * 60)

        return True


fact_checker = FactChecker()
