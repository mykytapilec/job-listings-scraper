
"""Tests for CSV job listing export."""

import csv

from job_scraper.exporter import export_job_listings


def test_export_job_listings_creates_csv_file(tmp_path):
    """Test that job listings are exported to a CSV file."""
    output_path = tmp_path / "jobs.csv"

    job_listings = [
        {
            "title": "Python Developer",
            "company": "Example Company",
            "location": "Warsaw, Poland",
            "url": "https://example.com/jobs/1",
        }
    ]

    export_job_listings(job_listings, output_path)

    assert output_path.exists()

    with output_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert reader.fieldnames == [
        "title",
        "company",
        "location",
        "url",
    ]
    assert rows == job_listings


def test_export_job_listings_handles_empty_list(tmp_path):
    """Test that an empty list produces a CSV file with headers."""
    output_path = tmp_path / "empty.csv"

    export_job_listings([], output_path)

    with output_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert reader.fieldnames == [
        "title",
        "company",
        "location",
        "url",
    ]
    assert rows == []


def test_export_job_listings_creates_parent_directories(tmp_path):
    """Test that missing parent directories are created."""
    output_path = tmp_path / "exports" / "jobs.csv"

    export_job_listings([], output_path)

    assert output_path.exists()


def test_export_job_listings_supports_unicode(tmp_path):
    """Test that Unicode characters are preserved in CSV output."""
    output_path = tmp_path / "jobs.csv"

    job_listings = [
        {
            "title": "Python Developer",
            "company": "Łódź Technologies",
            "location": "Kraków, Poland",
            "url": "https://example.com/jobs/1",
        }
    ]

    export_job_listings(job_listings, output_path)

    with output_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert rows == job_listings


def test_export_job_listings_ignores_extra_fields(tmp_path):
    """Test that unexpected fields are excluded from CSV output."""
    output_path = tmp_path / "jobs.csv"

    job_listings = [
        {
            "title": "Python Developer",
            "company": "Example Company",
            "location": "Warsaw",
            "url": "https://example.com/jobs/1",
            "extra": "Unexpected data",
        }
    ]

    export_job_listings(job_listings, output_path)

    with output_path.open(encoding="utf-8", newline="") as csv_file:
        reader = csv.DictReader(csv_file)
        rows = list(reader)

    assert list(rows[0].keys()) == [
        "title",
        "company",
        "location",
        "url",
    ]
    assert "extra" not in rows[0]
