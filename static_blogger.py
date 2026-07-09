#!/usr/bin/env python3

import json

from core.config import config
from core.content_engine import content_engine
from core.deduplicator import deduplicator
from core.logger import logger
from core.news_fetcher import news_fetcher


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
                continue

            logger.info(f"Generating package for: {topic}")

            package = content_engine.generate(topic)

            logger.info("=" * 60)
            logger.info("UNIFIED PACKAGE RECEIVED")
            logger.info("=" * 60)

            print(
                json.dumps(
                    package,
                    indent=4,
                    ensure_ascii=False
                )
            )

            return

    logger.info("No topic available.")


if __name__ == "__main__":
    main()
