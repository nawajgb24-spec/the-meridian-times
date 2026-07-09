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

        start_time = time.time()

        logger.info("=" * 60)
        logger.info("RETRY ENGINE STARTED")
        logger.info("=" * 60)

        for attempt in range(retries):

            try:

                logger.info(
                    f"Attempt {attempt + 1}/{retries}"
                )

                result = function()

                elapsed = round(
                    time.time() - start_time,
                    2
                )

                logger.info(
                    f"Retry Engine Success ({elapsed}s)"
                )

                logger.info("=" * 60)

                return result

            except ClientError as e:

                last_error = e

                message = str(e)

                logger.warning(message)

                if "GenerateRequestsPerDay" in message:

                    logger.error(
                        "Daily quota exhausted."
                    )

                    raise DailyQuotaExceeded()

                if (

                    "RESOURCE_EXHAUSTED" in message

                    or "429" in message

                ):

                    if attempt >= len(delays):

                        logger.error(
                            "Retry limit reached."
                        )

                        raise TemporaryRateLimit()

                    delay = delays[attempt]

                    jitter = random.randint(0, 5)

                    total = delay + jitter

                    logger.info(
                        f"Waiting {total} seconds..."
                    )

                    time.sleep(total)

                    continue

                raise

            except Exception as e:

                last_error = e

                logger.warning(str(e))

                if attempt >= len(delays):

                    logger.error(
                        "Retry limit reached."
                    )

                    raise

                delay = delays[attempt]

                jitter = random.randint(0, 5)

                total = delay + jitter

                logger.info(
                    f"Waiting {total} seconds..."
                )

                time.sleep(total)

        elapsed = round(
            time.time() - start_time,
            2
        )

        logger.error(
            f"Retry Engine Failed ({elapsed}s)"
        )

        logger.info("=" * 60)

        raise last_error


retry = Retry()
