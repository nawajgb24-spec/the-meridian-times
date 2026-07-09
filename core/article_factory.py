from core.article import Article
from core.slugify import slugify
from core.text_utils import word_count, reading_time


class ArticleFactory:

    def create(
        self,
        draft,
        seo
    ):

        slug = seo.slug.strip() if seo.slug else slugify(draft.title)

        article = Article(

            title=draft.title,

            slug=slug,

            category=draft.category,

            summary=draft.summary,

            content=draft.content,

            featured_image=draft.featured_image,

            tags=seo.tags,

            keywords=seo.secondary_keywords,

            seo_title=seo.seo_title,

            seo_description=seo.meta_description

        )

        article.word_count = word_count(
            draft.content
        )

        article.reading_time = reading_time(
            draft.content
        )

        return article


article_factory = ArticleFactory()
