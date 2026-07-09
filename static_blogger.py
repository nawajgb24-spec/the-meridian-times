#!/usr/bin/env python3

import random

from core.article_factory import article_factory
from core.config import config
from core.content_engine import content_engine
from core.deduplicator import deduplicator
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.publisher import publisher
from core.retry import (
    DailyQuotaExceeded,
    TemporaryRateLimit,
)


def main():

    logger.info("=" * 60)
    logger.info("THE MERIDIAN TIMES ENGINE STARTED")
    logger.info("=" * 60)

    all_topics = []
    seen = set()

    for category in config.get("categories", default=[]):

        logger.info(f"Collecting topics: {category}")

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
            all_topics.append(topic)

    random.shuffle(all_topics)

    logger.info(f"Collected {len(all_topics)} unique topics")

    for topic in all_topics:

        if deduplicator.exists(topic):
            continue

        logger.info(f"Selected Topic: {topic}")

        try:

            package = content_engine.generate(topic)

            article = article_factory.create_from_package(
                package
            )

            publisher.publish(article)

            logger.info(
                f"Published: {article.title}"
            )

            logger.info("=" * 60)
            logger.info("ENGINE FINISHED")
            logger.info("=" * 60)

            return

        except DailyQuotaExceeded:

            logger.warning("=" * 60)
            logger.warning("DAILY GEMINI QUOTA EXHAUSTED")
            logger.warning("Publishing skipped.")
            logger.warning("Workflow completed successfully.")
            logger.warning("=" * 60)

            return

        except TemporaryRateLimit:

            logger.warning(
                "Temporary rate limit reached."
            )

            continue

        except Exception as e:

            logger.exception(e)

            continue

    logger.info("No article published.")

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
