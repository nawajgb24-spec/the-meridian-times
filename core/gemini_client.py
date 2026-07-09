import os

from google import genai

from core.logger import logger


class GeminiClient:

    def __init__(self):

        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise RuntimeError("GEMINI_API_KEY secret not found.")

        self.client = genai.Client(api_key=api_key)

        logger.info("Gemini client initialized.")


gemini = GeminiClient()
