from core.audit_logger import audit_logger
from core.database import database
from core.homepage_builder import homepage_builder
from core.html_builder import html_builder
from core.image_generator import image_generator


class Publisher:

    def publish(self, article):

        image_info = image_generator.generate(
            article
        )

        article.featured_image = image_info[
            "filename"
        ]

        database.add(article)

        html_builder.build(article)

        homepage_builder.build()

        audit_logger.log(

            status="published",

            article=article

        )


publisher = Publisher()
