import time

from google.genai.errors import ClientError

from core.logger import logger


class Retry:

    def run(

        self,

        function,

        retries=3,

        delay=30

    ):

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                return function()

            except ClientError as e:

                last_error = e

                message = str(e)

                logger.warning(

                    f"Attempt {attempt}/{retries} failed: {message}"

                )

                # Daily quota exhausted → don't retry
                if (
                    "GenerateRequestsPerDay" in message
                    or "PerDay" in message
                ):

                    logger.error(

                        "Daily Gemini quota exhausted. Stopping retries."

                    )

                    raise

                # Temporary rate limit → retry
                if (
                    "RESOURCE_EXHAUSTED" in message
                    or "429" in message
                ):

                    if attempt < retries:

                        logger.info(

                            f"Retrying in {delay} seconds..."

                        )

                        time.sleep(delay)

                        continue

                raise

            except Exception as e:

                last_error = e

                logger.warning(

                    f"Attempt {attempt}/{retries} failed: {e}"

                )

                if attempt < retries:

                    logger.info(

                        f"Retrying in {delay} seconds..."

                    )

                    time.sleep(delay)

                else:

                    raise

        raise last_error


retry = Retry()
