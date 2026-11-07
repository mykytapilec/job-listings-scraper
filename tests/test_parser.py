
"""Tests for the HTML job listings parser."""

from job_scraper.parser import parse_job_listings


TEST_HTML = """
<html>
    <body>
        <div class="card">
            <div class="card-content">
                <h2 class="title is-5">Python Developer</h2>
                <h3 class="subtitle is-6">Example Company</h3>
                <p class="location">Warsaw, Poland</p>
            </div>
            <footer class="card-footer">
                <a class="card-footer-item" href="jobs/python-developer.html">
                    Apply
                </a>
            </footer>
        </div>
    </body>
</html>
"""


def test_parse_job_listings_returns_job_data():
    """Test that all job fields are extracted correctly."""
    result = parse_job_listings(TEST_HTML)

    assert len(result) == 1
    assert result[0] == {
        "title": "Python Developer",
        "company": "Example Company",
        "location": "Warsaw, Poland",
        "url": "https://realpython.github.io/fake-jobs/jobs/python-developer.html",
    }


def test_parse_job_listings_handles_missing_fields():
    """Test that missing HTML elements produce empty strings."""
    html = """
    <html>
        <body>
            <div class="card">
                <div class="card-content">
                    <h2 class="title">Python Developer</h2>
                </div>
            </div>
        </body>
    </html>
    """

    result = parse_job_listings(html)

    assert len(result) == 1
    assert result[0] == {
        "title": "Python Developer",
        "company": "",
        "location": "",
        "url": "",
    }


def test_parse_job_listings_returns_empty_list_without_cards():
    """Test that HTML without job cards returns an empty list."""
    html = "<html><body><h1>No jobs found</h1></body></html>"

    result = parse_job_listings(html)

    assert result == []


def test_parse_job_listings_extracts_multiple_jobs():
    """Test that multiple job cards are extracted."""
    html = """
    <html>
        <body>
            <div class="card">
                <h2 class="title">Python Developer</h2>
                <h3 class="subtitle">Company One</h3>
                <p class="location">Warsaw</p>
                <footer class="card-footer">
                    <a href="jobs/python.html">Apply</a>
                </footer>
            </div>
            <div class="card">
                <h2 class="title">Backend Developer</h2>
                <h3 class="subtitle">Company Two</h3>
                <p class="location">Krakow</p>
                <footer class="card-footer">
                    <a href="jobs/backend.html">Apply</a>
                </footer>
            </div>
        </body>
    </html>
    """

    result = parse_job_listings(html)

    assert len(result) == 2
    assert result[0]["title"] == "Python Developer"
    assert result[1]["title"] == "Backend Developer"


def test_parse_job_listings_supports_custom_base_url():
    """Test that relative URLs use the provided base URL."""
    result = parse_job_listings(
        TEST_HTML,
        base_url="https://example.com/careers/",
    )

    assert result[0]["url"] == (
        "https://example.com/careers/jobs/python-developer.html"
    )
