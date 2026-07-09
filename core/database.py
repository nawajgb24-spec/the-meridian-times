import json
from pathlib import Path

from core.logger import logger

ARTICLES_FILE = Path("articles.json")


class Database:

    def __init__(self):

        self.reload()

    def reload(self):

        if not ARTICLES_FILE.exists():

            self.data = {

                "articles": []

            }

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            self.data = json.load(f)

    def save(self):

        with open(
            ARTICLES_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def add(self, article):

        self.data["articles"].append(
            article.to_dict()
        )

        self.save()

        logger.info(
            f"Saved article: {article.title}"
        )

    def articles(self):

        return self.data["articles"]


database = Database()
