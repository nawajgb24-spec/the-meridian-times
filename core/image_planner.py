from core.gemini_engine import engine


class ImagePlanner:

    def plan(self, outline: str):

        return engine.generate(
            "image_planner",
            {
                "OUTLINE": outline
            }
        )


image_planner = ImagePlanner()
