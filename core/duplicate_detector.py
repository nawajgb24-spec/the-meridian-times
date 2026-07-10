from core.logger import logger


class DuplicateDetector:

    def validate(self, article):

        logger.info("=" * 60)
        logger.info("DUPLICATE DETECTOR")
        logger.info("=" * 60)

        paragraphs = [

            p.strip()

            for p in article.content.split("\n")

            if p.strip()

        ]

        seen = set()

        duplicates = []

        for paragraph in paragraphs:

            normalized = " ".join(

                paragraph.lower().split()

            )

            if normalized in seen:

                duplicates.append(paragraph)

            else:

                seen.add(normalized)

        if duplicates:

            raise ValueError(

                f"Duplicate paragraphs detected ({len(duplicates)})"

            )

        logger.info("Duplicate Check Passed")

        logger.info("=" * 60)

        return True


duplicate_detector = DuplicateDetector()
