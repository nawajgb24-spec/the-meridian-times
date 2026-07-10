#!/usr/bin/env python3

from core.health_dashboard import health_dashboard
from core.logger import logger
from core.pipeline import pipeline


def show_dashboard():

    summary = health_dashboard.summary()

    logger.info("=" * 60)
    logger.info("HEALTH DASHBOARD")
    logger.info("=" * 60)
    logger.info(f"Published          : {summary['published']}")
    logger.info(f"Failed             : {summary['failed']}")
    logger.info(f"Validation Failed  : {summary['validation']}")
    logger.info(f"Quota Events       : {summary['quota']}")
    logger.info("=" * 60)


def main():

    logger.info("=" * 60)
    logger.info("THE MERIDIAN TIMES ENGINE STARTED")
    logger.info("=" * 60)

    try:

        pipeline.run()

    finally:

        show_dashboard()

        logger.info("=" * 60)
        logger.info("ENGINE FINISHED")
        logger.info("=" * 60)


if __name__ == "__main__":
    main()
