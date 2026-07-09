from pathlib import Path


PROMPTS_DIR = Path("prompts")


class PromptLoader:

    def load(self, name: str) -> str:

        file = PROMPTS_DIR / f"{name}.md"

        return file.read_text(
            encoding="utf-8"
        )


prompts = PromptLoader()
