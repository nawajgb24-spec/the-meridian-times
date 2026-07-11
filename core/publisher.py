from core.audit_logger import audit_logger
from core.category_builder import category_builder
from core.database import database
from core.homepage_builder import homepage_builder
from core.html_builder import html_builder
from core.image_generator import image_generator
from core.robots_builder import robots_builder
from core.rss_builder import rss_builder
from core.search_index_builder import search_index_builder
from core.sitemap_builder import sitemap_builder
from core.trending_engine import trending_engine


class Publisher:

    def publish(self, article):

        image_info = image_generator.generate(
            article
        )

        article.featured_image = image_info[
            "filename"
        ]

        article.trending_score = (
            trending_engine.score(
                article
            )
        )

        database.add(article)

        html_builder.build(article)

        homepage_builder.build()

        category_builder.build()

        sitemap_builder.build()

        robots_builder.build()

        rss_builder.build()

        search_index_builder.build()

        audit_logger.log(

            status="published",

            article=article

        )


publisher = Publisher()
