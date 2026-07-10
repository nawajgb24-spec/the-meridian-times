import json
from pathlib import Path

from core.logger import logger


AUDIT_FILE = Path("audit_log.json")


class HealthDashboard:

    def summary(self):

        if not AUDIT_FILE.exists():

            return {

                "published": 0,

                "failed": 0,

                "quota": 0,

                "validation": 0

            }

        data = json.loads(

            AUDIT_FILE.read_text(

                encoding="utf-8"

            )

        )

        events = data.get("events", [])

        result = {

            "published": 0,

            "failed": 0,

            "quota": 0,

            "validation": 0

        }

        for event in events:

            status = event.get("status", "")

            if status == "published":

                result["published"] += 1

            elif status == "publish_failed":

                result["failed"] += 1

            elif status == "daily_quota_exhausted":

                result["quota"] += 1

            elif status == "validation_failed":

                result["validation"] += 1

        logger.info(f"Dashboard: {result}")

        return result


health_dashboard = HealthDashboard()
