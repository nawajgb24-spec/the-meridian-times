from core.gemini_engine import engine
from core.parser import parser


class ContentEngine:

    def generate(self, topic: str):

        response = engine.generate(

            "content_engine",

            {

                "TOPIC": topic

            }

        )

        return parser.content(response)


content_engine = ContentEngine()
