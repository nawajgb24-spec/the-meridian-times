#!/usr/bin/env python3

import time

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

    max_articles = config.get("daily_articles", default=3)

    published = 0

    for category in categories:

        if published >= max_articles:
            break

        logger.info(f"Category: {category}")

        topics = news_fetcher.fetch(category)

        for topic in topics:

            if published >= max_articles:
                break

            if deduplicator.exists(topic):
                continue

            logger.info(f"Researching: {topic}")

            report = research.generate(topic)

            logger.info(report[:300])

            published += 1

            time.sleep(15)

            break

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
