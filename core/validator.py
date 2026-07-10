from core.logger import logger


class ValidationError(Exception):
    pass


class Validator:

    MIN_WORDS = 800

    def validate(self, article):

        logger.info("=" * 60)
        logger.info("CONTENT VALIDATION")
        logger.info("=" * 60)

        self._validate_required_fields(article)

        self._validate_word_count(article)

        self._validate_seo(article)

        self._validate_tags(article)

        self._validate_reading_time(article)

        logger.info("Validation Passed")
        logger.info("=" * 60)

        return True

    def _validate_required_fields(self, article):

        required = {

            "Title": article.title,

            "Summary": article.summary,

            "Content": article.content,

            "Slug": article.slug,

        }

        for name, value in required.items():

            if not str(value).strip():

                raise ValidationError(f"{name} is empty.")

    def _validate_word_count(self, article):

        words = len(article.content.split())

        if words < self.MIN_WORDS:

            raise ValidationError(

                f"Content too short ({words} words)."

            )

    def _validate_seo(self, article):

        if not article.seo_title.strip():

            raise ValidationError(

                "SEO title missing."

            )

        if not article.seo_description.strip():

            raise ValidationError(

                "SEO description missing."

            )

    def _validate_tags(self, article):

        if not article.tags:

            raise ValidationError(

                "Tags missing."

            )

        if len(article.tags) < 3:

            raise ValidationError(

                "Minimum 3 tags required."

            )

    def _validate_reading_time(self, article):

        if article.reading_time <= 0:

            raise ValidationError(

                "Invalid reading time."

            )


validator = Validator()
