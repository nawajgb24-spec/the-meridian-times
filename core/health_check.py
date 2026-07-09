from pathlib import Path

from core.logger import logger


class HealthCheck:

    def run(self):

        logger.info("=" * 60)
        logger.info("HEALTH CHECK STARTED")
        logger.info("=" * 60)

        required_paths = [

            "config.json",

            "articles.json",

            "posts",

            "prompts",

            "core"

        ]

        ok = True

        for item in required_paths:

            path = Path(item)

            if path.exists():

                logger.info(f"[OK] {item}")

            else:

                logger.error(f"[MISSING] {item}")

                ok = False

        logger.info("=" * 60)

        if ok:

            logger.info("HEALTH CHECK PASSED")

        else:

            logger.error("HEALTH CHECK FAILED")

        logger.info("=" * 60)

        return ok


health_check = HealthCheck()
