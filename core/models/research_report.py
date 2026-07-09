from dataclasses import dataclass, field


@dataclass
class ResearchReport:

    topic: str

    category: str

    summary: str

    facts: list = field(default_factory=list)

    timeline: list = field(default_factory=list)

    people: list = field(default_factory=list)

    organizations: list = field(default_factory=list)

    locations: list = field(default_factory=list)

    keywords: list = field(default_factory=list)

    source_links: list = field(default_factory=list)
