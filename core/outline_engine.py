from core.gemini_engine import engine
from core.parser import parser


class OutlineEngine:

    def generate(self, research_report):

        response = engine.generate(

            "outline",

            {

                "RESEARCH": research_report.to_dict()

            }

        )

        return parser.outline(response)


outline = OutlineEngine()
