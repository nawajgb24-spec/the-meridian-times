import json
from html import escape
from pathlib import Path

from core.logger import logger
from core.template_engine import template_engine


ARTICLES_FILE = Path("articles.json")
INDEX_FILE = Path("index.html")


class HomepageBuilder:

    FEATURED_LIMIT = 5
    TRENDING_LIMIT = 10
    LATEST_LIMIT = 30

    def build(self):

        if not ARTICLES_FILE.exists():
            logger.warning("articles.json not found.")
            return

        with open(ARTICLES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        articles = data.get("articles", [])

        latest = sorted(
            articles,
            key=lambda x: x.get("published_at", ""),
            reverse=True
        )[:self.LATEST_LIMIT]

        trending = sorted(
            articles,
            key=lambda x: x.get("trending_score", 0),
            reverse=True
        )[:self.TRENDING_LIMIT]

        featured = trending[:self.FEATURED_LIMIT]

        def render_cards(items, heading=3):
            html = ""
            for article in items:
                html += f"""
<article class="news-card">
<a class="news-link" href="posts/{article.get('slug','')}.html">
<div class="news-card-body">
<div class="news-category">{escape(str(article.get('category','General')))}</div>
<h{heading} class="news-title">{escape(str(article.get('title','')))}</h{heading}>
<p class="news-summary">{escape(str(article.get('summary','')))}</p>
<div class="news-footer"><span class="read-more">Read More →</span></div>
</div>
</a>
</article>
"""
            return html

        hero = ""
        if featured:
            a = featured[0]
            hero = f"""
<section class="hero">
<div>
<h1>{escape(str(a.get('title','')))}</h1>
<p>{escape(str(a.get('summary','')))}</p>
</div>
</section>
"""

        header = template_engine.load("header.html")
        footer = template_engine.load("footer.html")

        html = template_engine.render(
            "homepage.html",
            {
                "HEADER": header,
                "FOOTER": footer,
                "HERO": hero,
                "FEATURED": render_cards(featured,2),
                "TRENDING": render_cards(trending,3),
                "LATEST": render_cards(latest,3),
            },
        )

        INDEX_FILE.write_text(html, encoding="utf-8")
        logger.info("Homepage generated.")


homepage_builder = HomepageBuilder()
