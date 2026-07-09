#!/usr/bin/env python3

import time

from core.config import config
from core.deduplicator import deduplicator
from core.editor_engine import editor
from core.journalist_engine import journalist
from core.logger import logger
from core.news_fetcher import news_fetcher
from core.outline_engine import outline
from core.research_engine import research
from core.seo_engine import seo


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

    completed = 0

    for category in categories:

        if completed >= articles_per_run:
            break

        topics = news_fetcher.fetch(category)

        for topic in topics:

            if completed >= articles_per_run:
                break

            if deduplicator.exists(topic):
                continue

            logger.info(f"Topic: {topic}")

            try:

                research_report = research.generate(topic)

                logger.info("✅ Research Complete")

                outline_plan = outline.generate(research_report)

                logger.info("✅ Outline Complete")

                article = journalist.write(outline_plan)

                logger.info("✅ Article Complete")

                article = editor.edit(article)

                logger.info("✅ Editor Complete")

                seo_data = seo.generate(article)

                logger.info("✅ SEO Complete")

                logger.info("=" * 60)
                logger.info(article.title)
                logger.info("=" * 60)

                completed += 1

                time.sleep(50)

            except Exception as e:

                logger.exception(e)

            break

    logger.info("=" * 60)
    logger.info("ENGINE FINISHED")
    logger.info("=" * 60)


if __name__ == "__main__":
    main()
