from pathlib import Path


class TemplateEngine:

    TEMPLATE_DIR = Path("templates")

    def load(self, template_name):

        file = self.TEMPLATE_DIR / template_name

        if not file.exists():

            raise FileNotFoundError(

                f"Template not found: {template_name}"

            )

        return file.read_text(

            encoding="utf-8"

        )

    def render(

        self,

        template_name,

        context=None

    ):

        html = self.load(

            template_name

        )

        if context:

            for key, value in context.items():

                html = html.replace(

                    "{{" + key + "}}",

                    str(value)

                )

        return html


template_engine = TemplateEngine()
