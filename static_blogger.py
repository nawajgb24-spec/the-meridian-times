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

    stop = False

    for category in categories:

        if stop:
            break

        logger.info(f"Fetching {category}")

        try:
            topics = news_fetcher.fetch(category)
        except Exception as e:
            logger.exception(e)
            continue

        for topic in topics:

            if deduplicator.exists(topic):
                continue

            try:

                logger.info(f"Topic: {topic}")

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

                if completed >= articles_per_run:
                    stop = True
                    break

                time.sleep(60)

            except Exception as e:

                logger.exception(e)
                break

    logger.info("=" * 60)
    logger.info(f"Generated Articles
