#!/usr/bin/env python3

from core.article_factory import article_factory
from core.config import config
from core.content_engine import content_engine
from core.deduplicator import deduplicator
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.publisher import publisher


def main():

    logger.info("=" * 60)
    logger.info("THE MERIDIAN TIMES ENGINE STARTED")
    logger.info("=" * 60)

    articles_per_run = config.get(
        "publishing",
        "articles_per_run",
        default=1
    )

    completed = 0

    for category in config.get("categories", default=[]):

        logger.info(f"Category: {category}")

        topics = news_fetcher.fetch(category)

        for topic in topics:

            if deduplicator.exists(topic):
                continue

            logger.info(f"Generating: {topic}")

            try:

                package = content_engine.generate(topic)

                article = article_factory.create_from_package(
                    package
                )

                publisher.publish(article)

                logger.info(
                    f"Published: {article.title}"
                )

                completed += 1

                if completed >= articles_per_run:

                    logger.info(
                        "Daily limit reached."
                    )

                    logger.info("=" * 60)
                    logger.info("ENGINE FINISHED")
                    logger.info("=" * 60)

                    return

            except Exception as e:

                logger.exception(e)

                break

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
