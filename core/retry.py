import time

from google.genai.errors import ClientError

from core.logger import logger


class DailyQuotaExceeded(Exception):
    pass


class TemporaryRateLimit(Exception):
    pass


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

                message = str(e)

                last_error = e

                logger.warning(message)

                # Daily quota exhausted
                if "GenerateRequestsPerDay" in message:

                    raise DailyQuotaExceeded()

                # Temporary quota
                if (

                    "RESOURCE_EXHAUSTED" in message

                    or "429" in message

                ):

                    if attempt == retries:

                        raise TemporaryRateLimit()

                    logger.info(

                        f"Retrying in {delay} seconds..."

                    )

                    time.sleep(delay)

                    continue

                raise

        raise last_error


retry = Retry()
