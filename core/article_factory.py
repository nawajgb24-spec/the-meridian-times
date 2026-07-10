from core.models.article import Article
from core.slug_manager import slug_manager


class ArticleFactory:

    def create_from_package(self, package):

        article_data = package["article"]
        seo_data = package["seo"]

        slug = slug_manager.unique_slug(
            seo_data["slug"]
        )

        return Article(

            title=article_data["title"],

            slug=slug,

            category=article_data["category"],

            summary=article_data["summary"],

            content=article_data["content"],

            featured_image=article_data.get(
                "featured_image",
                ""
            ),

            tags=seo_data.get(
                "tags",
                []
            ),

            keywords=article_data.get(
                "keywords",
                []
            ),

            source_links=article_data.get(
                "source_links",
                []
            ),

            reading_time=article_data.get(
                "reading_time",
                0
            ),

            word_count=article_data.get(
                "word_count",
                0
            ),

            seo_title=seo_data["seo_title"],

            seo_description=seo_data[
                "meta_description"
            ]

        )


article_factory = ArticleFactory()
