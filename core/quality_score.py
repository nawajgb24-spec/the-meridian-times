from core.logger import logger
from core.readability import readability
from core.fact_checker import fact_checker
from core.duplicate_detector import duplicate_detector


class QualityScore:

    MAX_SCORE = 100

    def evaluate(self, article):

        logger.info("=" * 60)
        logger.info("QUALITY SCORE ENGINE")
        logger.info("=" * 60)

        score = self.MAX_SCORE

        try:
            fact_checker.validate(article)
        except Exception:
            score -= 30

        try:
            duplicate_detector.validate(article)
        except Exception:
            score -= 20

        try:
            readability.validate(article)
        except Exception:
            score -= 20

        if len(article.tags) < 5:
            score -= 10

        if article.word_count < 900:
            score -= 20

        score = max(0, score)

        logger.info(
            f"Final Quality Score: {score}/100"
        )

        logger.info("=" * 60)

        return score


quality_score = QualityScore()
