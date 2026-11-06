
"""Tests for the page fetching module."""

from unittest.mock import Mock, patch

import pytest
import requests

from job_scraper.fetcher import fetch_page


TEST_URL = "https://realpython.github.io/fake-jobs/"
TEST_HTML = "<html><body><h1>Job Listings</h1></body></html>"


@patch("job_scraper.fetcher.requests.get")
def test_fetch_page_returns_html(mock_get):
    """Test that fetch_page returns the HTML response."""
    mock_response = Mock()
    mock_response.text = TEST_HTML
    mock_get.return_value = mock_response

    result = fetch_page(TEST_URL)

    assert result == TEST_HTML
    mock_get.assert_called_once_with(TEST_URL, timeout=10.0)
    mock_response.raise_for_status.assert_called_once()


@patch("job_scraper.fetcher.requests.get")
def test_fetch_page_raises_http_error(mock_get):
    """Test that HTTP errors are propagated."""
    mock_response = Mock()
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Client Error"
    )
    mock_get.return_value = mock_response

    with pytest.raises(requests.exceptions.HTTPError):
        fetch_page(TEST_URL)


@patch("job_scraper.fetcher.requests.get")
def test_fetch_page_raises_connection_error(mock_get):
    """Test that connection errors are propagated."""
    mock_get.side_effect = requests.exceptions.ConnectionError(
        "Connection failed"
    )

    with pytest.raises(requests.exceptions.ConnectionError):
        fetch_page(TEST_URL)


@patch("job_scraper.fetcher.requests.get")
def test_fetch_page_uses_custom_timeout(mock_get):
    """Test that a custom timeout is passed to the request."""
    mock_response = Mock()
    mock_response.text = TEST_HTML
    mock_get.return_value = mock_response

    fetch_page(TEST_URL, timeout=5.0)

    mock_get.assert_called_once_with(TEST_URL, timeout=5.0)
