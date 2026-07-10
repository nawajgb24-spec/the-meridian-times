import re

from core.database import database


class SlugManager:

    def unique_slug(self, slug: str) -> str:

        slug = self._normalize(slug)

        existing = {

            self._normalize(

                article.get("slug", "")

            )

            for article in database.articles()

        }

        if slug not in existing:

            return slug

        counter = 2

        while True:

            candidate = f"{slug}-{counter}"

            if candidate not in existing:

                return candidate

            counter += 1

    @staticmethod
    def _normalize(slug: str) -> str:

        slug = slug.strip().lower()

        slug = slug.replace("_", "-")

        slug = re.sub(r"[^a-z0-9\- ]", "", slug)

        slug = slug.replace(" ", "-")

        slug = re.sub(r"-+", "-", slug)

        return slug.strip("-")


slug_manager = SlugManager()
