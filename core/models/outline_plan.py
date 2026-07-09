from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class OutlinePlan:

    title: str

    category: str

    sections: list[str] = field(default_factory=list)

    image_sections: list[str] = field(default_factory=list)

    estimated_words: int = 1000

    reading_time: int = 5

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def to_dict(self):

        return {

            "title": self.title,

            "category": self.category,

            "sections": self.sections,

            "image_sections": self.image_sections,

            "estimated_words": self.estimated_words,

            "reading_time": self.reading_time,

            "created_at": self.created_at

        }
