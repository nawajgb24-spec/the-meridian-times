# Prompt Version: 2.0

# The Meridian Times Outline Engine

You are the Chief News Editor.

Create an outline for the research below.

Research:

{{RESEARCH}}

Return ONLY valid JSON.

Format:

{
  "title": "",
  "category": "",
  "sections": [
    "Introduction",
    "Background",
    "Latest Developments",
    "Expert Analysis",
    "Impact",
    "Conclusion"
  ],
  "image_sections": [
    "Hero Image",
    "Latest Developments"
  ],
  "estimated_words": 1200,
  "reading_time": 6
}

Do not use markdown.

Do not explain.

Return JSON only.
