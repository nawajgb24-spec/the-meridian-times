from core.article import Article


class ArticleFactory:

    def create_from_package(self, package: dict):

        article = package["article"]

        seo = package["seo"]

        research = package["research"]

        return Article(

            title=article["title"],

            slug=seo["slug"],

            category=article["category"],

            summary=article["summary"],

            content=article["content"],

            featured_image="",

            tags=seo.get("tags", []),

            keywords=research.get("keywords", []),

            source_links=research.get("source_links", []),

            seo_title=seo["seo_title"],

            seo_description=seo["meta_description"],

            word_count=len(article["content"].split()),

            reading_time=max(
                1,
                len(article["content"].split()) // 200
            )

        )


article_factory = ArticleFactory()
