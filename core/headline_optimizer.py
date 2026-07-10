import re

from core.logger import logger


class HeadlineOptimizer:

    MIN_LENGTH = 30
    MAX_LENGTH = 70

    def optimize(self, title: str) -> str:

        logger.info("=" * 60)
        logger.info("HEADLINE OPTIMIZER")
        logger.info("=" * 60)

        title = re.sub(

            r"\s+",

            " ",

            title.strip()

        )

        if len(title) > self.MAX_LENGTH:

            title = title[: self.MAX_LENGTH].rstrip()

        logger.info(

            f"Optimized Headline: {title}"

        )

        logger.info("=" * 60)

        return title

    def validate(self, title: str):

        if len(title) < self.MIN_LENGTH:

            raise ValueError(

                "Headline too short."

            )

        if len(title) > self.MAX_LENGTH:

            raise ValueError(

                "Headline too long."

            )

        return True


headline_optimizer = HeadlineOptimizer()
