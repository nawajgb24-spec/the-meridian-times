from core.database import database
from core.html_builder import html_builder
from core.logger import logger


class Publisher:

    def publish(self, article):

        database.add(article)

        html_builder.build(article)

        logger.info(
            f"Published: {article.title}"
        )


publisher = Publisher()
