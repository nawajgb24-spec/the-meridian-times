from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Article:

    title: str

    slug: str

    category: str

    summary: str

    content: str

    featured_image: str

    tags: list = field(default_factory=list)

    keywords: list = field(default_factory=list)

    source_links: list = field(default_factory=list)

    id: str = field(default_factory=lambda: uuid4().hex)

    author: str = "The Meridian Times"

    status: str = "published"

    published_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    updated_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    reading_time: int = 0

    word_count: int = 0

    seo_title: str = ""

    seo_description: str = ""

    def to_dict(self):

        return {

            "id": self.id,

            "title": self.title,

            "slug": self.slug,

            "category": self.category,

            "summary": self.summary,

            "content": self.content,

            "featured_image": self.featured_image,

            "author": self.author,

            "status": self.status,

            "published_at": self.published_at,

            "updated_at": self.updated_at,

            "reading_time": self.reading_time,

            "word_count": self.word_count,

            "tags": self.tags,

            "keywords": self.keywords,

            "source_links": self.source_links,

            "seo": {

                "title": self.seo_title,

                "description": self.seo_description

            }

        }
