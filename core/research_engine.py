from core.gemini_engine import engine


class ResearchEngine:

    def generate(self, topic: str):

        return engine.generate(
            "researcher",
            {
                "TOPIC": topic
            }
        )


research = ResearchEngine()
