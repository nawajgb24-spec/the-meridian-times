from core.logger import logger


class ProductionPipeline:

    def run(self):

        logger.info("=" * 60)
        logger.info("PRODUCTION PIPELINE STARTED")
        logger.info("=" * 60)

        self.health_check()

        self.collect_topics()

        self.generate_article()

        self.publish()

        self.finish()

    def health_check(self):

        pass

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
