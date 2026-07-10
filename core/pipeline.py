from core.health_check import health_check
from core.logger import logger


class ProductionPipeline:

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

        pass

    def generate_article(self):

        pass

    def publish(self):

        pass

    def finish(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE FINISHED")
        logger.info("=" * 60)


pipeline = ProductionPipeline()
