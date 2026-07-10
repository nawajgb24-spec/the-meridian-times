from core.logger import logger
from core.quality_score import quality_score


class EditorialDecision:

    PUBLISH_SCORE = 80

    REVIEW_SCORE = 60

    def decide(self, article):

        logger.info("=" * 60)
        logger.info("EDITORIAL DECISION ENGINE")
        logger.info("=" * 60)

        score = quality_score.evaluate(article)

        if score >= self.PUBLISH_SCORE:

            decision = "publish"

        elif score >= self.REVIEW_SCORE:

            decision = "review"

        else:

            decision = "reject"

        logger.info(
            f"Decision: {decision.upper()}"
        )

        logger.info(
            f"Quality Score: {score}/100"
        )

        logger.info("=" * 60)

        return {

            "decision": decision,

            "score": score

        }


editorial_decision = EditorialDecision()
