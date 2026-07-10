from core.logger import logger


class CategoryConfidence:

    KEYWORDS = {
        "Tech": [
            "ai", "artificial intelligence", "software",
            "technology", "chip", "google", "microsoft",
            "apple", "openai", "robot"
        ],
        "Business": [
            "company", "business", "market",
            "investment", "startup", "economy"
        ],
        "Stock News": [
            "stock", "shares", "nasdaq",
            "dow", "sensex", "nifty", "earnings"
        ],
        "Sports": [
            "football", "cricket", "tennis",
            "nba", "fifa", "olympics", "match"
        ],
        "Anime": [
            "anime", "manga", "one piece",
            "naruto", "bleach", "dragon ball"
        ],
        "Lifestyle": [
            "health", "travel", "fashion",
            "food", "fitness", "wellness"
        ],
        "Food & Nutrition": [
            "nutrition", "diet", "recipe",
            "vitamin", "protein", "meal"
        ],
        "World": []
    }

    def score(self, article):

        logger.info("=" * 60)
        logger.info("CATEGORY CONFIDENCE")
        logger.info("=" * 60)

        text = (
            article.title + " " +
            article.summary + " " +
            article.content
        ).lower()

        scores = {}

        for category, words in self.KEYWORDS.items():

            score = sum(
                1 for word in words
                if word in text
            )

            scores[category] = score

        best_category = max(
            scores,
            key=scores.get
        )

        logger.info(
            f"Suggested Category: {best_category}"
        )

        logger.info("=" * 60)

        return {
            "current": article.category,
            "suggested": best_category,
            "scores": scores
        }


category_confidence = CategoryConfidence()
