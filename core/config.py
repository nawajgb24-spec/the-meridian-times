import json
from pathlib import Path

CONFIG_PATH = Path("config.json")


class Config:

    def __init__(self):

        self.reload()

    def reload(self):

        with open(CONFIG_PATH, "r", encoding="utf-8") as f:

            self.data = json.load(f)

    def get(self, *keys, default=None):

        value = self.data

        for key in keys:

            if isinstance(value, dict):

                value = value.get(key)

            else:

                return default

            if value is None:

                return default

        return value


config = Config()
