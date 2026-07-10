import time

from core.logger import logger


class PerformanceMonitor:

    def __init__(self):

        self.timers = {}

    def start(self, name):

        self.timers[name] = {

            "start": time.perf_counter()

        }

    def stop(self, name):

        if name not in self.timers:

            return

        self.timers[name]["elapsed"] = round(

            time.perf_counter()

            - self.timers[name]["start"],

            3

        )

    def report(self):

        logger.info("=" * 60)
        logger.info("PERFORMANCE REPORT")
        logger.info("=" * 60)

        total = 0.0

        for name, data in self.timers.items():

            elapsed = data.get(

                "elapsed",

                0

            )

            total += elapsed

            logger.info(

                f"{name:<20}: {elapsed:.3f}s"

            )

        logger.info("-" * 60)

        logger.info(

            f"{'Total':<20}: {total:.3f}s"

        )

        logger.info("=" * 60)


performance_monitor = PerformanceMonitor()
