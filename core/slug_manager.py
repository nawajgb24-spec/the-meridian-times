from core.database import database


class SlugManager:

    def unique_slug(self, slug: str) -> str:

        slug = slug.strip().lower()

        existing = {

            article["slug"].lower()

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


slug_manager = SlugManager()
