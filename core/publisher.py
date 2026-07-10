from core.audit_logger import audit_logger
from core.database import database
from core.homepage_builder import homepage_builder
from core.html_builder import html_builder


class Publisher:

    def publish(self, article):

        database.add(article)

        html_builder.build(article)

        homepage_builder.build()

        audit_logger.log(

            status="published",

            article=article

        )


publisher = Publisher()
