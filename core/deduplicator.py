from core.database import database


class Deduplicator:

    def exists(self, title: str) -> bool:

        title = title.strip().lower()

        for article in database.articles():

            if article["title"].strip().lower() == title:

                return True

        return False


deduplicator = Deduplicator()
