import json

from core.models.article_draft import ArticleDraft
from core.models.editorial_report import EditorialReport
from core.models.outline_plan import OutlinePlan
from core.models.research_report import ResearchReport
from core.models.seo_data import SEOData


class Parser:

    @staticmethod
    def research(text: str) -> ResearchReport:

        data = json.loads(text)

        research = data.get("research", data)

        return ResearchReport(

            topic=research.get("topic", ""),

            category=research.get("category", ""),

            summary=research.get("summary", ""),

            facts=research.get("facts", []),

            timeline=research.get("timeline", []),

            people=research.get("people", []),

            organizations=research.get("organizations", []),

            locations=research.get("locations", []),

            keywords=research.get("keywords", []),

            source_links=research.get("source_links", [])

        )

    @staticmethod
    def outline(text: str) -> OutlinePlan:

        data = json.loads(text)

        outline = data.get("outline", data)

        return OutlinePlan(

            title=outline.get("title", ""),

            category=outline.get("category", ""),

            sections=outline.get("sections", []),

            image_sections=outline.get("image_sections", []),

            estimated_words=outline.get(
                "estimated_words",
                1000
            ),

            reading_time=outline.get(
                "reading_time",
                5
            )

        )

    @staticmethod
    def article(text: str) -> ArticleDraft:

        data = json.loads(text)

        article = data.get("article", data)

        return ArticleDraft(

            title=article.get("title", ""),

            summary=article.get("summary", ""),

            content=article.get("content", ""),

            category=article.get("category", ""),

            slug=article.get("slug", ""),

            featured_image=article.get(
                "featured_image",
                ""
            ),

            tags=article.get(
                "tags",
                []
            ),

            keywords=article.get(
                "keywords",
                []
            ),

            source_links=article.get(
                "source_links",
                []
            ),

            word_count=article.get(
                "word_count",
                0
            ),

            reading_time=article.get(
                "reading_time",
                0
            )

        )

    @staticmethod
    def seo(text: str) -> SEOData:

        data = json.loads(text)

        seo = data.get("seo", data)

        return SEOData(

            seo_title=seo.get("seo_title", ""),

            meta_description=seo.get(
                "meta_description",
                ""
            ),

            slug=seo.get("slug", ""),

            focus_keyword=seo.get(
                "focus_keyword",
                ""
            ),

            secondary_keywords=seo.get(
                "secondary_keywords",
                []
            ),

            tags=seo.get(
                "tags",
                []
            ),

            image_alt=seo.get(
                "image_alt",
                ""
            ),

            image_caption=seo.get(
                "image_caption",
                ""
            ),

            canonical_url=seo.get(
                "canonical_url",
                ""
            )

        )

    @staticmethod
    def report(text: str) -> EditorialReport:

        data = json.loads(text)

        report = data.get("report", data)

        return EditorialReport(

            editorial_score=report.get(
                "editorial_score",
                0
            ),

            originality=report.get(
                "originality",
                0
            ),

            fact_consistency=report.get(
                "fact_consistency",
                0
            ),

            readability=report.get(
                "readability",
                0
            ),

            grammar=report.get(
                "grammar",
                0
            ),

            structure=report.get(
                "structure",
                0
            ),

            seo=report.get(
                "seo",
                0
            ),

            copyright_risk=report.get(
                "copyright_risk",
                0
            ),

            decision=report.get(
                "decision",
                ""
            )

        )

    @staticmethod
    def content(text: str):

        return json.loads(text)


parser = Parser()
