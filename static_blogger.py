#!/usr/bin/env python3

from core.logger import logger
from core.config import config
from core.news_fetcher import news_fetcher
from core.deduplicator import deduplicator
from core.research_engine import research


def main():

    logger.info("=" * 60)
    logger.info("THE MERIDIAN TIMES ENGINE STARTED")
    logger.info("=" * 60)

    categories = config.get("categories", default=[])

    for category in categories:

        logger.info(f"Category: {category}")

        topics = news_fetcher.fetch(category)

        for topic in topics:

            if deduplicator.exists(topic):

                logger.info(f"Skipped: {topic}")

                continue

            logger.info(f"Researching: {topic}")

            report = research.generate(topic)

            logger.info(report[:300])

            break

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":

    main()
