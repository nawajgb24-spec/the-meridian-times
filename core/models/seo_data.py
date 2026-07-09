from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class SEOData:

    seo_title: str

    meta_description: str

    slug: str

    focus_keyword: str

    secondary_keywords: list[str] = field(default_factory=list)

    tags: list[str] = field(default_factory=list)

    image_alt: str = ""

    image_caption: str = ""

    canonical_url: str = ""

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def to_dict(self):

        return {

            "seo_title": self.seo_title,

            "meta_description": self.meta_description,

            "slug": self.slug,

            "focus_keyword": self.focus_keyword,

            "secondary_keywords": self.secondary_keywords,

            "tags": self.tags,

            "image_alt": self.image_alt,

            "image_caption": self.image_caption,

            "canonical_url": self.canonical_url,

            "created_at": self.created_at

        }
