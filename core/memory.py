from core.database import database


class Memory:

    def articles(self):

        return database.articles()

    def slugs(self):

        return {

            article.get("slug")

            for article in self.articles()

        }

    def titles(self):

        return {

            article.get("title")

            for article in self.articles()

        }

    def categories(self):

        return [

            article.get("category")

            for article in self.articles()

        ]


memory = Memory()
