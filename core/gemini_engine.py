import json

from core.gemini_client import gemini
from core.prompt_loader import prompts


class GeminiEngine:

    def generate(
        self,
        prompt_name: str,
        variables: dict
    ):

        prompt = prompts.load(prompt_name)

        for key, value in variables.items():

            prompt = prompt.replace(
                "{{" + key + "}}",
                str(value)
            )

        response = gemini.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text.strip()


engine = GeminiEngine()
