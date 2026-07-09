from core.database import database
from core.homepage_builder import homepage_builder
from core.html_builder import html_builder
from core.logger import logger


class Publisher:

    def publish(self, article):

        database.add(article)

        html_builder.build(article)

        homepage_builder.build()

        logger.info(
            f"Published: {article.title}"
        )


publisher = Publisher()
