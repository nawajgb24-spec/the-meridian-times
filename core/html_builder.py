from html import escape
from pathlib import Path

from core.internal_linker import internal_linker
from core.logger import logger


POSTS_DIR = Path("posts")
POSTS_DIR.mkdir(exist_ok=True)


class HtmlBuilder:

    def build(self, article):

        related = internal_linker.build(article)

        related_html = ""

        if related:

            related_html += "<section><h2>Related Articles</h2><ul>"

            for item in related:

                related_html += f"""
<li>
<a href="{item['slug']}.html">
{escape(item['title'])}
</a>
</li>
"""

            related_html += "</ul></section>"

        html = f"""<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{escape(article.seo_title or article.title)}</title>

<meta name="description" content="{escape(article.seo_description or article.summary)}">

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
