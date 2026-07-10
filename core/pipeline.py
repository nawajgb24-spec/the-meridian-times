from core.article_factory import article_factory
from core.config import config
from core.content_engine import content_engine
from core.deduplicator import deduplicator
from core.health_check import health_check
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.publisher import publisher
from core.regeneration_engine import regeneration_engine
from core.validator import (
    validator,
    ValidationError,
)


class ProductionPipeline:

    MAX_REGENERATION_ATTEMPTS = 1

    def __init__(self):

        self.topics = []
        self.selected_topic = None
        self.package = None
        self.article = None

    def run(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE STARTED")
        logger.info("=" * 60)

        if not health_check.run():

            logger.error("Health Check Failed.")

            self.finish()

            return

        self.collect_topics()

        if not self.topics:

            logger.warning("No topics collected.")

            self.finish()

            return

        for topic in self.topics:

            if self.process_topic(topic):

                break

        else:

            logger.warning(
                "No article could be published."
            )

        self.finish()

    def collect_topics(self):

        logger.info("Collecting Topics...")

        self.topics.clear()

        seen = set()

        for category in config.get(
            "categories",
            default=[]
        ):

            logger.info(
                f"Category: {category}"
            )

            try:

                topics = news_fetcher.fetch(
                    category
                )

            except Exception as e:

                logger.exception(e)

                continue

            for topic in topics:

                key = topic.strip().lower()

                if key in seen:

                    continue

                seen.add(key)

                self.topics.append(topic)

        logger.info(
            f"{len(self.topics)} unique topics collected."
        )

    def process_topic(self, topic):

        self.selected_topic = topic

        if deduplicator.exists(topic):

            logger.info(
                f"Duplicate skipped: {topic}"
            )

            return False

        logger.info(
            f"Processing: {topic}"
        )

        try:

            self.package = content_engine.generate(
                topic
            )

        except Exception as e:

            logger.exception(e)

            return False

        for attempt in range(

            self.MAX_REGENERATION_ATTEMPTS + 1

        ):

            try:

                self.article = article_factory.create_from_package(
                    self.package
                )

                validator.validate(
                    self.article
                )

                publisher.publish(
                    self.article
                )

                logger.info(
                    f"Published: {self.article.title}"
                )

                return True

            except ValidationError as e:

                logger.warning(
                    f"Validation failed: {e}"
                )

                if attempt >= self.MAX_REGENERATION_ATTEMPTS:

                    logger.error(
                        "Maximum regeneration attempts reached."
                    )

                    return False

                logger.info(
                    "Running self-healing regeneration..."
                )

                try:

                    self.package = regeneration_engine.improve(
                        self.package,
                        str(e)
                    )

                except Exception as regen_error:

                    logger.exception(
                        regen_error
                    )

                    return False

            except Exception as e:

                logger.exception(e)

                return False

        return False

    def finish(self):

        logger.info("=" * 60)

        logger.info(
            "PRODUCTION PIPELINE FINISHED"
        )

        logger.info("=" * 60)


pipeline = ProductionPipeline()
