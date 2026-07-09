import re

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

        text = response.text.strip()

        if text.startswith("```"):

            text = re.sub(
                r"^```(?:json)?",
                "",
                text,
                flags=re.IGNORECASE
            )

            text = re.sub(
                r"```$",
                "",
                text
            )

            text = text.strip()

        return text


engine = GeminiEngine()
