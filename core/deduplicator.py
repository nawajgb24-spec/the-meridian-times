from core.database import database


class Deduplicator:

    def exists(self, title: str) -> bool:

        normalized = self._normalize(title)

        for article in database.articles():

            article_title = self._normalize(

                article.get("title", "")

            )

            article_slug = self._normalize(

                article.get("slug", "")

            )

            if (

                normalized == article_title

                or normalized == article_slug

            ):

                return True

        return False

    @staticmethod
    def _normalize(text: str) -> str:

        return (

            text.strip()

            .lower()

            .replace("-", " ")

            .replace("_", " ")

        )


deduplicator = Deduplicator()
