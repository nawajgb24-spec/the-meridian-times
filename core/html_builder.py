from pathlib import Path

from core.logger import logger


POSTS_DIR = Path("posts")

POSTS_DIR.mkdir(
    exist_ok=True
)


class HtmlBuilder:

    def build(self, article):

        html = f"""<!DOCTYPE html>
<html lang="en">
<head>

<meta charset="UTF-8">

<title>{article.title}</title>

<meta name="description" content="{article.summary}">

</head>

<body>

<h1>{article.title}</h1>

<p>{article.summary}</p>

{article.content}

</body>
</html>
"""

        file = POSTS_DIR / f"{article.slug}.html"

        file.write_text(
            html,
            encoding="utf-8"
        )

        logger.info(
            f"HTML Generated: {file.name}"
        )


html_builder = HtmlBuilder()
