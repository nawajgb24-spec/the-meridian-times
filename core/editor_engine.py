from core.gemini_engine import engine


class EditorEngine:

    def edit(self, article):

        response = engine.generate(

            "editor",

            {

                "ARTICLE": article.content

            }

        )

        article.content = response

        return article


editor = EditorEngine()
