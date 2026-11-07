
"""HTML parser for extracting job listings."""

from urllib.parse import urljoin

from bs4 import BeautifulSoup


DEFAULT_BASE_URL = "https://realpython.github.io/fake-jobs/"


def parse_job_listings(
    html: str,
    base_url: str = DEFAULT_BASE_URL,
) -> list[dict[str, str]]:
    """Parse job listings from HTML content."""
    soup = BeautifulSoup(html, "html.parser")
    job_listings = []

    for card in soup.select(".card"):
        title_element = card.select_one(".title")
        company_element = card.select_one(".subtitle")
        location_element = card.select_one(".location")

        apply_link = next(
            (
                link
                for link in card.select(".card-footer a[href]")
                if link.get_text(strip=True).lower() == "apply"
            ),
            None,
        )

        title = title_element.get_text(strip=True) if title_element else ""
        company = company_element.get_text(strip=True) if company_element else ""
        location = (
            location_element.get_text(strip=True)
            if location_element
            else ""
        )

        job_url = (
            urljoin(base_url, apply_link["href"])
            if apply_link
            else ""
        )

        job_listings.append(
            {
                "title": title,
                "company": company,
                "location": location,
                "url": job_url,
            }
        )

    return job_listings
