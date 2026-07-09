from dataclasses import dataclass, field


@dataclass
class SEOData:

    title: str

    description: str

    slug: str

    keywords: list = field(default_factory=list)

    tags: list = field(default_factory=list)
