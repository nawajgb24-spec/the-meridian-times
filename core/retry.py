import random
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

        delays=(10, 20, 40, 80)

    ):

        last_error = None

        retries = len(delays) + 1

        for attempt in range(retries):

            try:

                return function()

            except ClientError as e:

                last_error = e

                message = str(e)

                logger.warning(message)

                # Daily quota exhausted
                if "GenerateRequestsPerDay" in message:

                    raise DailyQuotaExceeded()

                # Temporary quota / rate limit
                if (

                    "RESOURCE_EXHAUSTED" in message

                    or "429" in message

                ):

                    if attempt >= len(delays):

                        raise TemporaryRateLimit()

                    delay = delays[attempt]

                    jitter = random.randint(0, 5)

                    total = delay + jitter

                    logger.info(

                        f"Retrying after {total} seconds..."

                    )

                    time.sleep(total)

                    continue

                raise

            except Exception as e:

                last_error = e

                if attempt >= len(delays):

                    raise

                delay = delays[attempt]

                jitter = random.randint(0, 5)

                total = delay + jitter

                logger.warning(str(e))

                logger.info(

                    f"Retrying after {total} seconds..."

                )

                time.sleep(total)

        raise last_error


retry = Retry()
