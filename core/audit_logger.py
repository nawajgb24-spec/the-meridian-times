import json
from datetime import datetime
from pathlib import Path

from core.logger import logger


AUDIT_FILE = Path("audit_log.json")


class AuditLogger:

    def __init__(self):

        if not AUDIT_FILE.exists():

            AUDIT_FILE.write_text(

                json.dumps({"events": []}, indent=4),

                encoding="utf-8"

            )

    def log(

        self,

        status,

        article=None,

        reason=""

    ):

        data = json.loads(

            AUDIT_FILE.read_text(

                encoding="utf-8"

            )

        )

        event = {

            "timestamp": datetime.utcnow().isoformat(),

            "status": status,

            "reason": reason

        }

        if article:

            event.update({

                "title": article.title,

                "slug": article.slug,

                "category": article.category,

                "word_count": article.word_count,

                "reading_time": article.reading_time

            })

        data["events"].append(event)

        AUDIT_FILE.write_text(

            json.dumps(

                data,

                indent=4

            ),

            encoding="utf-8"

        )

        logger.info(

            f"Audit Logged: {status}"

        )


audit_logger = AuditLogger()
