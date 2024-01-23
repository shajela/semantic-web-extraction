import asyncio
import pprint

from extractor import extract
from schemas import schema
from scrape import ascrape_playwright

# TESTING
if __name__ == "__main__":
    token_limit = 4000

    url = "https://careers.walmart.com/us/jobs/WD1625381-usa-software-engineer-ii"

    async def scrape_with_playwright(url: str, tags, **kwargs):
        html_content = await ascrape_playwright(url, tags)

        print("Extracting content with LLM")

        html_content_fits_context_window_llm = html_content[:token_limit]

        extracted_content = extract(**kwargs,
                                    content=html_content_fits_context_window_llm)

        pprint.pprint(extracted_content)

    # Scrape and Extract with LLM
    asyncio.run(scrape_with_playwright(
        url=url,
        tags=["span"],
        schema=schema
    ))
