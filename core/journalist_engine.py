from core.gemini_engine import engine


class JournalistEngine:

    def write(self, research: str):

        return engine.generate(
            "journalist",
            {
                "RESEARCH": research
            }
        )


journalist = JournalistEngine()
