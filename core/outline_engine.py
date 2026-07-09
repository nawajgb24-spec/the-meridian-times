from core.gemini_engine import engine


class OutlineEngine:

    def generate(self, research: str):

        return engine.generate(
            "outline",
            {
                "RESEARCH": research
            }
        )


outline = OutlineEngine()
