import xml.etree.ElementTree as ET

import requests

from core.logger import logger


RSS_URL = "https://news.google.com/rss/search"


class NewsFetcher:

    def __init__(self):

        self.session = requests.Session()

        self.session.headers.update({

            "User-Agent": "The Meridian Times"

        })

    def fetch(self, category):

        logger.info(f"Fetching {category}")

        response = self.session.get(

            RSS_URL,

            params={

                "q": category,

                "hl": "en-US",

                "gl": "US",

                "ceid": "US:en"

            },

            timeout=30

        )

        response.raise_for_status()

        root = ET.fromstring(response.text)

        topics = []

        for item in root.findall(".//item"):

            title = item.findtext("title")

            if not title:

                continue

            title = title.split(" - ")[0].strip()

            if title not in topics:

                topics.append(title)

        logger.info(f"{len(topics)} topics found")

        return topics


news_fetcher = NewsFetcher()
