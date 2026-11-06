
"""HTTP client for fetching web page content."""

import requests


def fetch_page(url: str, timeout: float = 10.0) -> str:
    """Fetch a web page and return its HTML content.

    Args:
        url: The URL of the page to fetch.
        timeout: Maximum number of seconds to wait for a response.

    Returns:
        The HTML content of the page.

    Raises:
        requests.exceptions.RequestException: If the request fails.
    """
    response = requests.get(url, timeout=timeout)
    response.raise_for_status()

    return response.text
