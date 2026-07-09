#!/usr/bin/env python3

import time

from core.config import config
from core.deduplicator import deduplicator
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.research_engine import research


def main():

    logger.info("=" * 60)
    logger.info("THE MERIDIAN TIMES ENGINE STARTED")
    logger.info("=" * 60)

    categories = config.get("categories", default=[])

    articles_per_run = config.get(
        "publishing",
        "articles_per_run",
        default=1
    )

    published = 0

    for category in categories:

        if published >= articles_per_run:
            break

        logger.info(f"Category: {category}")

        try:

            topics = news_fetcher.fetch(category)

        except Exception as e:

            logger.exception(e)

            continue

        for topic in topics:

            if published >= articles_per_run:
                break

            if deduplicator.exists(topic):

                logger.info(f"Duplicate skipped: {topic}")

                continue

            logger.info(f"Researching: {topic}")

            try:

                report = research.generate(topic)

                logger.info(report[:500])

                published += 1

                logger.info(
                    f"Completed {published}/{articles_per_run}"
                )

                # Free Gemini Tier Safety
                time.sleep(50)

            except Exception as e:

                logger.exception(e)

                continue

            break

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":

    main()
