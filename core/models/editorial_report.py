from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class EditorialReport:

    editorial_score: int

    originality: int

    fact_consistency: int

    readability: int

    grammar: int

    structure: int

    seo: int

    copyright_risk: str

    decision: str

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )

    def approved(self) -> bool:

        return (

            self.editorial_score >= 95

            and self.copyright_risk.upper() == "LOW"

            and self.decision.upper() == "APPROVE"

        )

    def to_dict(self):

        return {

            "editorial_score": self.editorial_score,

            "originality": self.originality,

            "fact_consistency": self.fact_consistency,

            "readability": self.readability,

            "grammar": self.grammar,

            "structure": self.structure,

            "seo": self.seo,

            "copyright_risk": self.copyright_risk,

            "decision": self.decision,

            "created_at": self.created_at

        }
