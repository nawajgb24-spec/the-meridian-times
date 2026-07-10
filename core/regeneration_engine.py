from core.gemini_engine import engine
from core.parser import parser


class RegenerationEngine:

    def expand(self, package):

        article = package["article"]
        seo = package["seo"]

        prompt = f"""
You are a professional newspaper editor.

Expand the following news article.

Rules:

- Keep every fact accurate.
- Do NOT invent information.
- Preserve the original structure.
- Expand every section naturally.
- Target 1000-1200 words.
- Return ONLY valid JSON.
- Keep the existing SEO.

ARTICLE JSON:

{article}

SEO JSON:

{seo}
"""

        response = engine.generate(

            "regeneration_engine",

            {

                "PROMPT": prompt

            }

        )

        return parser.content(response)


regeneration_engine = RegenerationEngine()
