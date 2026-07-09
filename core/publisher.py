from core.database import database
from core.logger import logger


class Publisher:

    def publish(self, article):

        articles = database.articles()

        articles.insert(0, article.to_dict())

        database.save()

        logger.info(
            f"Published: {article.title}"
        )


publisher = Publisher()
