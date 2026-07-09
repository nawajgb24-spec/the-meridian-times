from dataclasses import dataclass


@dataclass
class EditorialReport:

    editorial_score: int

    originality: int

    readability: int

    grammar: int

    structure: int

    seo: int

    copyright_risk: str

    decision: str
