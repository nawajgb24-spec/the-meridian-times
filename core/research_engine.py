from core.gemini_engine import engine
from core.parser import parser


class ResearchEngine:

    def generate(self, topic: str):

        response = engine.generate(

            "researcher",

            {

                "TOPIC": topic

            }

        )

        return parser.research(response)


research = ResearchEngine()
