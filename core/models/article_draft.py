from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ArticleDraft:

    title: str

    summary: str

    content: str

    category: str

    slug: str

    featured_image: str = ""

    tags: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    word_count: int = 0

    reading_time: int = 0

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def to_dict(self):

        return {

            "title": self.title,

            "summary": self.summary,

            "content": self.content,

            "category": self.category,

            "slug": self.slug,

            "featured_image": self.featured_image,

            "tags": self.tags,

            "keywords": self.keywords,

            "word_count": self.word_count,

            "reading_time": self.reading_time,

            "created_at": self.created_at

        }
