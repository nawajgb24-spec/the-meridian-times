from core.gemini_engine import engine
from core.parser import parser


class RegenerationEngine:

    def improve(

        self,

        package,

        reason: str

    ):

        prompt = f"""
You are the Editor-in-Chief of The Meridian Times.

The previous article failed validation.

Validation Failure:

{reason}

Your task:

1. Fix every issue.

2. Keep every verified fact.

3. Never invent information.

4. Improve readability.

5. Improve SEO.

6. Improve structure.

7. Remove duplicated content.

8. Ensure 1000-1200 words.

9. Return EXACTLY the same JSON structure.

Previous JSON:

{package}
"""

        response = engine.generate(

            "regeneration_engine",

            {

                "PROMPT": prompt

            }

        )

        return parser.content(response)


regeneration_engine = RegenerationEngine()
