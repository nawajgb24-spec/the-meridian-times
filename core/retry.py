import time

from core.logger import logger


class Retry:

    def run(

        self,

        function,

        retries=3,

        delay=30,

        exceptions=(Exception,)

    ):

        last_error = None

        for attempt in range(1, retries + 1):

            try:

                return function()

            except exceptions as e:

                last_error = e

                logger.warning(

                    f"Attempt {attempt}/{retries} failed: {e}"

                )

                if attempt < retries:

                    logger.info(

                        f"Retrying in {delay} seconds..."

                    )

                    time.sleep(delay)

        raise last_error


retry = Retry()
