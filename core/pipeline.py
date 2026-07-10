from core.article_factory import article_factory
from core.config import config
from core.content_engine import content_engine
from core.deduplicator import deduplicator
from core.health_check import health_check
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.publisher import publisher
from core.validator import validator, ValidationError


class ProductionPipeline:

    def __init__(self):

        self.topics = []
        self.package = None
        self.article = None
        self.selected_topic = None

    def run(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE STARTED")
        logger.info("=" * 60)

        if not self.health_check():

            logger.info("=" * 60)
            logger.info("PIPELINE STOPPED")
            logger.info("=" * 60)
            return

        self.collect_topics()

        self.generate_article()

        self.publish()

        self.finish()

    def health_check(self):

        logger.info("Running Health Check...")

        return health_check.run()

    def collect_topics(self):

        logger.info("Collecting Topics...")

        seen = set()

        self.topics.clear()

        categories = config.get(
            "categories",
            default=[]
        )

        for category in categories:

            logger.info(f"Category: {category}")

            try:

                topics = news_fetcher.fetch(category)

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
            f"Collected {len(self.topics)} unique topics."
        )

    def generate_article(self):

        self.package = None
        self.article = None

        for topic in self.topics:

            if deduplicator.exists(topic):

                logger.info(
                    f"Skipping duplicate: {topic}"
                )

                continue

            self.selected_topic = topic

            logger.info(
                f"Generating article: {topic}"
            )

            self.package = content_engine.generate(
                topic
            )

            logger.info(
                "Content generation completed."
            )

            break

        if self.package is None:

            logger.warning(
                "No eligible topic found."
            )

    def publish(self):

        if self.package is None:

            logger.warning(
                "Nothing to publish."
            )

            return

        self.article = article_factory.create_from_package(
            self.package
        )

        try:

            validator.validate(
                self.article
            )

        except ValidationError as e:

            logger.error(
                f"Validation failed: {e}"
            )

            self.article = None

            return

        logger.info(
            f"Validated: {self.article.title}"
        )

        publisher.publish(
            self.article
        )

        logger.info(
            "Publishing completed."
        )

    def finish(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE FINISHED")
        logger.info("=" * 60)


pipeline = ProductionPipeline()
