from core.config import config
from core.health_check import health_check
from core.logger import logger
from core.news_fetcher import news_fetcher


class ProductionPipeline:

    def __init__(self):

        self.topics = []

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

        pass

    def publish(self):

        pass

    def finish(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE FINISHED")
        logger.info("=" * 60)


pipeline = ProductionPipeline()
