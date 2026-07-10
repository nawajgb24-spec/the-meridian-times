from pathlib import Path


class ImageMetadata:

    def build(self, article):

        return {
            "filename": article.featured_image,
            "alt": article.seo_title or article.title,
            "title": article.title,
            "caption": article.summary,
            "path": str(
                Path("images") / article.featured_image
            )
        }


image_metadata = ImageMetadata()
