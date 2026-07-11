import json
from html import escape
from pathlib import Path

from core.internal_linker import internal_linker
from core.logger import logger


POSTS_DIR = Path("posts")
POSTS_DIR.mkdir(exist_ok=True)

SITE_URL = "https://themeridiantimes.com"


class HtmlBuilder:

    def build(self, article):

        related = internal_linker.build(article)

        related_html = ""

        if related:

            related_html += "<section><h2>Related Articles</h2><ul>"

            for item in related:

                related_html += f"""
<li>
<a href="{SITE_URL}/posts/{item['slug']}.html">
{escape(item['title'])}
</a>
</li>
"""

            related_html += "</ul></section>"

        page_url = (
            f"{SITE_URL}/posts/{article.slug}.html"
        )

        image_url = (
            f"{SITE_URL}/images/{article.featured_image}"
            if article.featured_image
            else ""
        )

        structured_data = {
            "@context": "https://schema.org",
            "@type": "NewsArticle",
            "headline": article.title,
            "description": article.summary,
            "datePublished": article.published_at,
            "dateModified": article.updated_at,
            "author": {
                "@type": "Organization",
                "name": article.author
            },
            "publisher": {
                "@type": "Organization",
                "name": "The Meridian Times"
            },
            "mainEntityOfPage": page_url,
            "image": image_url,
            "keywords": article.keywords
        }

        html = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>{escape(article.seo_title or article.title)}</title>

<meta name="description"
content="{escape(article.seo_description or article.summary)}">

<meta name="keywords"
content="{escape(', '.join(article.keywords))}">

<link rel="canonical"
href="{page_url}">

<meta property="og:type"
content="article">

<meta property="og:title"
content="{escape(article.title)}">

<meta property="og:description"
content="{escape(article.summary)}">

<meta property="og:url"
content="{page_url}">

<meta property="og:image"
content="{image_url}">

<meta property="article:published_time"
content="{article.published_at}">

<meta property="article:modified_time"
content="{article.updated_at}">

<meta name="twitter:card"
content="summary_large_image">

<meta name="twitter:title"
content="{escape(article.title)}">

<meta name="twitter:description"
content="{escape(article.summary)}">

<meta name="twitter:image"
content="{image_url}">

<script type="application/ld+json">

{json.dumps(structured_data, ensure_ascii=False, indent=2)}

</script>

</head>

<body>

<header>

<h1>{escape(article.title)}</h1>

<p>{escape(article.summary)}</p>

</header>

<main>

{article.content}

{related_html}

</main>

</body>

</html>
"""

        file = POSTS_DIR / f"{article.slug}.html"

        file.write_text(

            html,

            encoding="utf-8"

        )

        logger.info(
            f"Generated HTML: {file.name}"
        )


html_builder = HtmlBuilder()
