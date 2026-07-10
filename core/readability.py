import re

from core.logger import logger


class Readability:

    MIN_SCORE = 60

    def score(self, article):

        logger.info("=" * 60)
        logger.info("READABILITY ANALYZER")
        logger.info("=" * 60)

        text = article.content

        sentences = max(
            len(re.findall(r"[.!?]+", text)),
            1
        )

        words = max(
            len(text.split()),
            1
        )

        avg_sentence = words / sentences

        score = max(
            0,
            min(
                100,
                round(
                    100 - ((avg_sentence - 15) * 2),
                    2
                )
            )
        )

        logger.info(
            f"Readability Score: {score}"
        )

        logger.info("=" * 60)

        return score

    def validate(self, article):

        score = self.score(article)

        if score < self.MIN_SCORE:

            raise ValueError(

                f"Readability score too low ({score})"

            )

        return True


readability = Readability()
