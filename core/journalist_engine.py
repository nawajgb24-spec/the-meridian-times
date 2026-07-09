from core.gemini_engine import engine
from core.parser import parser


class JournalistEngine:

    def write(self, outline_plan):

        response = engine.generate(

            "journalist",

            {

                "RESEARCH": "\n".join(outline_plan.sections)

            }

        )

        return parser.article(response)


journalist = JournalistEngine()
