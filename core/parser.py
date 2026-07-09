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

        return ResearchReport(

            topic=data["topic"],
            category=data["category"],
            summary=data["summary"],
            facts=data.get("facts", []),
            timeline=data.get("timeline", []),
            people=data.get("people", []),
            organizations=data.get("organizations", []),
            locations=data.get("locations", []),
            keywords=data.get("keywords", []),
            source_links=data.get("source_links", [])

        )

    @staticmethod
    def outline(text: str) -> OutlinePlan:

        data = json.loads(text)

        return OutlinePlan(

            title=data["title"],
            category=data["category"],
            sections=data.get("sections", []),
            image_sections=data.get("image_sections", []),
            estimated_words=data.get("estimated_words", 1000),
            reading_time=data.get("reading_time", 5)

        )

    @staticmethod
    def article(text: str) -> ArticleDraft:

        data = json.loads(text)

        return ArticleDraft(

            title=data["title"],
            summary=data["summary"],
            content=data["content"],
            category=data["category"],
            slug=data["slug"],
            featured_image=data.get("featured_image", ""),
            tags=data.get("tags", []),
            keywords=data.get("keywords", []),
            word_count=data.get("word_count", 0),
            reading_time=data.get("reading_time", 0)

        )

    @staticmethod
    def seo(text: str) -> SEOData:

        data = json.loads(text)

        return SEOData(

            seo_title=data["seo_title"],
            meta_description=data["meta_description"],
            slug=data["slug"],
            focus_keyword=data.get("focus_keyword", ""),
            secondary_keywords=data.get("secondary_keywords", []),
            tags=data.get("tags", []),
            image_alt=data.get("image_alt", ""),
            image_caption=data.get("image_caption", ""),
            canonical_url=data.get("canonical_url", "")

        )

    @staticmethod
    def report(text: str) -> EditorialReport:

        data = json.loads(text)

        return EditorialReport(

            editorial_score=data["editorial_score"],
            originality=data["originality"],
            fact_consistency=data["fact_consistency"],
            readability=data["readability"],
            grammar=data["grammar"],
            structure=data["structure"],
            seo=data["seo"],
            copyright_risk=data["copyright_risk"],
            decision=data["decision"]

        )

    @staticmethod
    def content(text: str):

        return json.loads(text)


parser = Parser()
