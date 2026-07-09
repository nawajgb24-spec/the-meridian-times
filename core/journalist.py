from abc import ABC, abstractmethod

from core.article import Article
from core.researcher import ResearchReport


class Journalist(ABC):

    @abstractmethod
    def write(
        self,
        report: ResearchReport
    ) -> Article:
        """
        Convert research into a complete article.
        """
