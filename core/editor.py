from abc import ABC, abstractmethod

from core.article import Article


class Editor(ABC):

    @abstractmethod
    def review(
        self,
        article: Article
    ) -> Article:
        """
        Review and improve the article before publishing.
        """
