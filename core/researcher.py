from dataclasses import dataclass


@dataclass
class ResearchReport:

    topic: str

    category: str

    facts: list

    timeline: list

    keywords: list

    people: list

    locations: list

    source_links: list

    summary: str
