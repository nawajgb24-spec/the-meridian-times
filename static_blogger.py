#!/usr/bin/env python3

from core.logger import logger
from core.config import config
from core.news_fetcher import news_fetcher


def main():

    logger.info("===================================")
    logger.info("The Meridian Times Engine Started")
    logger.info("===================================")

    categories = config.get("categories")

    logger.info(f"Loaded {len(categories)} categories.")

    for category in categories:

        topics = news_fetcher.fetch(category)

        logger.info(f"{category}: {len(topics)} topics")

    logger.info("Engine Finished")


if __name__ == "__main__":

    main()
