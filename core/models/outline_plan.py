from dataclasses import dataclass, field


@dataclass
class OutlinePlan:

    title: str

    sections: list = field(default_factory=list)

    image_sections: list = field(default_factory=list)

    estimated_words: int = 1000
