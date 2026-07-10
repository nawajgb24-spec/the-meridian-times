from core.logger import logger


class ValidationError(Exception):
    pass


class Validator:

    MIN_WORDS = 800

    def validate(self, article):

        logger.info("=" * 60)
        logger.info("CONTENT VALIDATION")
        logger.info("=" * 60)

        if not article.title.strip():

            raise ValidationError("Title is empty.")

        if not article.summary.strip():

            raise ValidationError("Summary is empty.")

        if not article.content.strip():

            raise ValidationError("Content is empty.")

        if not article.slug.strip():

            raise ValidationError("Slug is empty.")

        if not article.seo_title.strip():

            raise ValidationError("SEO title missing.")

        if not article.seo_description.strip():

            raise ValidationError("SEO description missing.")

        words = len(article.content.split())

        if words < self.MIN_WORDS:

            raise ValidationError(

                f"Content too short ({words} words)."

            )

        logger.info("Validation Passed")

        logger.info("=" * 60)

        return True


validator = Validator()
