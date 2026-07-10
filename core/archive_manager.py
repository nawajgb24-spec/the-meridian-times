import json
from pathlib import Path

from core.logger import logger


ARTICLES_FILE = Path("articles.json")
ARCHIVE_FILE = Path("archive.json")


class ArchiveManager:

    ARCHIVE_AFTER = 1000

    def rotate(self):

        if not ARTICLES_FILE.exists():

            return

        with open(
            ARTICLES_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)

        articles = data.get(
            "articles",
            []
        )

        if len(articles) <= self.ARCHIVE_AFTER:

            return

        archived = articles[:-self.ARCHIVE_AFTER]

        active = articles[-self.ARCHIVE_AFTER:]

        archive_data = {

            "articles": archived

        }

        with open(

            ARCHIVE_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                archive_data,

                f,

                indent=4,

                ensure_ascii=False

            )

        data["articles"] = active

        with open(

            ARTICLES_FILE,

            "w",

            encoding="utf-8"

        ) as f:

            json.dump(

                data,

                f,

                indent=4,

                ensure_ascii=False

            )

        logger.info(

            f"Archived {len(archived)} articles."

        )


archive_manager = ArchiveManager()
