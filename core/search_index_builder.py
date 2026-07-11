import json
from pathlib import Path

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
SEARCH_FILE = Path("search_index.json")


class SearchIndexBuilder:

    def build(self):

        if not ARTICLES_FILE.exists():

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        search = []

        for article in data.get(
            "articles",
            []
        ):

            search.append({

                "title": article["title"],

                "slug": article["slug"],

                "summary": article["summary"],

                "category": article["category"],

                "keywords": article.get(
                    "keywords",
                    []
                ),

                "tags": article.get(
                    "tags",
                    []
                )

            })

        SEARCH_FILE.write_text(

            json.dumps(

                search,

                indent=2,

                ensure_ascii=False

            ),

            encoding="utf-8"

        )

        logger.info(

            "search_index.json generated."

        )


search_index_builder = SearchIndexBuilder()
