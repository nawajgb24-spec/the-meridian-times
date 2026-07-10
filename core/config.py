import json
from pathlib import Path

from core.logger import logger


CONFIG_PATH = Path("config.json")


class Config:

    def __init__(self):

        self.reload()

    def reload(self):

        if not CONFIG_PATH.exists():

            raise FileNotFoundError(

                f"{CONFIG_PATH} not found."

            )

        with open(

            CONFIG_PATH,

            "r",

            encoding="utf-8"

        ) as f:

            self.data = json.load(f)

        logger.info("Configuration loaded.")

    def get(self, *keys, default=None):

        value = self.data

        for key in keys:

            if not isinstance(value, dict):

                return default

            value = value.get(key)

            if value is None:

                return default

        return value


config = Config()
