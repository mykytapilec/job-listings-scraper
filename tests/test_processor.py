
"""Tests for job listing data processing."""

from job_scraper.processor import process_job_listings


def test_process_job_listings_normalizes_whitespace():
    """Test that whitespace is normalized in job fields."""
    job_listings = [
        {
            "title": "  Python   Developer\n",
            "company": "  Example   Company ",
            "location": " Warsaw,   Poland ",
            "url": " https://example.com/jobs/1 ",
        }
    ]

    result = process_job_listings(job_listings)

    assert result == [
        {
            "title": "Python Developer",
            "company": "Example Company",
            "location": "Warsaw, Poland",
            "url": "https://example.com/jobs/1",
        }
    ]


def test_process_job_listings_handles_missing_fields():
    """Test that missing fields are replaced with empty strings."""
    job_listings = [
        {
            "title": "Python Developer",
        }
    ]

    result = process_job_listings(job_listings)

    assert result == [
        {
            "title": "Python Developer",
            "company": "",
            "location": "",
            "url": "",
        }
    ]


def test_process_job_listings_returns_empty_list():
    """Test that an empty input produces an empty output."""
    result = process_job_listings([])

    assert result == []


def test_process_job_listings_preserves_multiple_listings():
    """Test that all job listings are processed in the original order."""
    job_listings = [
        {
            "title": "Python Developer",
            "company": "Company One",
            "location": "Warsaw",
            "url": "https://example.com/jobs/1",
        },
        {
            "title": "Backend Developer",
            "company": "Company Two",
            "location": "Krakow",
            "url": "https://example.com/jobs/2",
        },
    ]

    result = process_job_listings(job_listings)

    assert len(result) == 2
    assert result[0]["title"] == "Python Developer"
    assert result[1]["title"] == "Backend Developer"


def test_process_job_listings_does_not_modify_original_data():
    """Test that processing does not mutate the original input."""
    job_listings = [
        {
            "title": "  Python Developer  ",
            "company": "Example Company",
            "location": "Warsaw",
            "url": "https://example.com/jobs/1",
        }
    ]

    original_title = job_listings[0]["title"]

    process_job_listings(job_listings)

    assert job_listings[0]["title"] == original_title


def test_process_job_listings_ignores_unexpected_fields():
    """Test that only supported job fields are returned."""
    job_listings = [
        {
            "title": "Python Developer",
            "company": "Example Company",
            "location": "Warsaw",
            "url": "https://example.com/jobs/1",
            "extra": "Unexpected data",
        }
    ]

    result = process_job_listings(job_listings)

    assert list(result[0].keys()) == [
        "title",
        "company",
        "location",
        "url",
    ]
