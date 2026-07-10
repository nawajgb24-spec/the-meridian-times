import hashlib
from pathlib import Path

from core.logger import logger


IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)


class ImageGenerator:

    def filename(self, article) -> str:

        slug = article.slug

        digest = hashlib.md5(
            slug.encode("utf-8")
        ).hexdigest()[:8]

        return f"{slug}-{digest}.webp"

    def generate(self, article):

        image_name = self.filename(article)

        image_path = IMAGES_DIR / image_name

        logger.info(
            f"Image placeholder prepared: {image_name}"
        )

        return {

            "filename": image_name,

            "path": str(image_path),

            "prompt": article.featured_image,

            "alt": article.seo_title or article.title

        }


image_generator = ImageGenerator()
