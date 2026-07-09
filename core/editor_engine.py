from core.gemini_engine import engine


class EditorEngine:

    def edit(self, article: str):

        return engine.generate(
            "editor",
            {
                "ARTICLE": article
            }
        )


editor = EditorEngine()
