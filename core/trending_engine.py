from datetime import datetime, timezone

from core.logger import logger


class TrendingEngine:

    def score(self, article):

        score = 0

        score += min(
            len(article.tags),
            10
        )

        score += min(
            len(article.keywords),
            10
        )

        score += min(
            article.word_count // 100,
            15
        )

        score += min(
            article.reading_time,
            10
        )

        try:

            published = datetime.fromisoformat(
                article.published_at
            )

            if published.tzinfo is None:

                published = published.replace(
                    tzinfo=timezone.utc
                )

            age_hours = (

                datetime.now(timezone.utc)

                - published

            ).total_seconds() / 3600

            freshness = max(

                0,

                20 - int(age_hours)

            )

            score += freshness

        except Exception:

            pass

        logger.info(

            f"Trending Score: {score}"

        )

        return score


trending_engine = TrendingEngine()
