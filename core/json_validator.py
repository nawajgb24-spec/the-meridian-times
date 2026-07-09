import json


class JsonValidator:

    @staticmethod
    def validate(text: str):

        try:

            return json.loads(text)

        except json.JSONDecodeError:

            return None
