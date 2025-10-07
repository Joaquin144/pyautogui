import os

import ollama

from src.logger.config import setup_logger

log = setup_logger("generate_ai_insights")


def generate_ai_insights(content: str) -> str:
    try:
        prompt = f"""
        You are a kind and loving AI assistant that extracts useful information from LinkedIn "About" section. Ignore spelling mistakes be lenient
Here is the raw text:

\"\"\"{content}\"\"\"

Extract and return a JSON with fields:
- summary: cleaned summary in 1–2 sentences praising that person
- keywords: list of important keywords/skills

Return only the JSON.
"""
        response = ollama.chat(
            model='mistral',
            messages=[
                {'role': 'user', 'content': prompt}
            ]
        )

        return response['message']['content'].strip()


    except Exception as e:
        log.error("Failed to generate AI Insights", e)
        return ""
