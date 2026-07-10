from pathlib import Path

from core.logger import logger


IMAGES_DIR = Path("images")
IMAGES_DIR.mkdir(exist_ok=True)


class ImageDownloader:

    def save(self, filename: str, image_bytes: bytes):

        path = IMAGES_DIR / filename

        path.write_bytes(image_bytes)

        logger.info(

            f"Image saved: {filename}"

        )

        return path

    def exists(self, filename: str):

        return (

            IMAGES_DIR / filename

        ).exists()


image_downloader = ImageDownloader()
