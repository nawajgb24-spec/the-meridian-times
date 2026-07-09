from core.gemini_engine import engine
from core.parser import parser


class SEOEngine:

    def generate(self, article):

        response = engine.generate(

            "seo",

            {

                "ARTICLE": article.content,

                "TITLE": article.title

            }

        )

        return parser.seo(response)


seo = SEOEngine()
