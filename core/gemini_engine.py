import re

from core.gemini_client import gemini
from core.prompt_loader import prompts
from core.retry import retry


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

        def request():

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

        return retry.run(
            function=request,
            retries=3,
            delay=30
        )


engine = GeminiEngine()
