import json
from datetime import datetime, timedelta
from pathlib import Path

from core.logger import logger


STATUS_FILE = Path("quota_status.json")


class QuotaManager:

    def __init__(self):

        self.status = self.load()

    def load(self):

        if STATUS_FILE.exists():

            try:

                return json.loads(

                    STATUS_FILE.read_text(

                        encoding="utf-8"

                    )

                )

            except Exception:

                pass

        return {

            "status": "ok",

            "retry_after": None,

            "updated_at": None

        }

    def save(self):

        STATUS_FILE.write_text(

            json.dumps(

                self.status,

                indent=4

            ),

            encoding="utf-8"

        )

    def set_daily_exhausted(self):

        self.status = {

            "status": "daily_exhausted",

            "retry_after": None,

            "updated_at": datetime.utcnow().isoformat()

        }

        self.save()

        logger.warning(

            "Daily Gemini quota exhausted."

        )

    def set_temporary(self, seconds):

        retry_time = (

            datetime.utcnow()

            + timedelta(seconds=seconds)

        )

        self.status = {

            "status": "temporary",

            "retry_after": retry_time.isoformat(),

            "updated_at": datetime.utcnow().isoformat()

        }

        self.save()

    def clear(self):

        self.status = {

            "status": "ok",

            "retry_after": None,

            "updated_at": datetime.utcnow().isoformat()

        }

        self.save()

    def can_run(self):

        if self.status["status"] == "ok":

            return True

        if self.status["status"] == "daily_exhausted":

            return False

        if self.status["status"] == "temporary":

            retry_after = self.status.get("retry_after")

            if retry_after:

                if datetime.utcnow() >= datetime.fromisoformat(retry_after):

                    self.clear()

                    return True

            return False

        return True


quota_manager = QuotaManager()
