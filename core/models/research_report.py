from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class ResearchReport:

    topic: str

    category: str

    summary: str

    facts: list[str] = field(default_factory=list)

    timeline: list[str] = field(default_factory=list)

    people: list[str] = field(default_factory=list)

    organizations: list[str] = field(default_factory=list)

    locations: list[str] = field(default_factory=list)

    keywords: list[str] = field(default_factory=list)

    source_links: list[str] = field(default_factory=list)

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def to_dict(self):

        return {

            "topic": self.topic,

            "category": self.category,

            "summary": self.summary,

            "facts": self.facts,

            "timeline": self.timeline,

            "people": self.people,

            "organizations": self.organizations,

            "locations": self.locations,

            "keywords": self.keywords,

            "source_links": self.source_links,

            "created_at": self.created_at

        }
