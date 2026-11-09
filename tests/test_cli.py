
"""Tests for the command-line interface."""

from unittest.mock import call

import pytest

from job_scraper import cli


def test_create_parser_uses_default_arguments() -> None:
    parser = cli.create_parser()

    args = parser.parse_args([])

    assert args.url == cli.DEFAULT_BASE_URL
    assert args.output == "jobs.csv"


def test_create_parser_accepts_custom_arguments() -> None:
    parser = cli.create_parser()

    args = parser.parse_args(
        [
            "--url",
            "https://example.com/jobs",
            "--output",
            "data/custom_jobs.csv",
        ]
    )

    assert args.url == "https://example.com/jobs"
    assert args.output == "data/custom_jobs.csv"


def test_main_runs_scraping_pipeline(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:
    html = "<html></html>"
    raw_listings = [
        {"title": "Python Developer", "company": "Example", "location": "Warsaw", "url": "https://example.com/job"}
    ]
    processed_listings = [
        {"title": "Python Developer", "company": "Example", "location": "Warsaw", "url": "https://example.com/job"}
    ]

    monkeypatch.setattr(
        "sys.argv",
        ["job_scraper", "--url", "https://example.com/jobs", "--output", "output/jobs.csv"],
    )

    fetch_mock = pytest.MonkeyPatch.context
    monkeypatch.setattr(cli, "fetch_page", lambda url: html)
    monkeypatch.setattr(
        cli,
        "parse_job_listings",
        lambda received_html, base_url: raw_listings,
    )
    monkeypatch.setattr(
        cli,
        "process_job_listings",
        lambda listings: processed_listings,
    )

    exported: list[tuple[list[dict[str, str]], str]] = []

    def fake_export(
        listings: list[dict[str, str]],
        output_path: str,
    ) -> None:
        exported.append((listings, output_path))

    monkeypatch.setattr(cli, "export_job_listings", fake_export)

    cli.main()

    assert exported == [(processed_listings, "output/jobs.csv")]
    assert capsys.readouterr().out == (
        "Exported 1 job listings to output/jobs.csv\n"
    )


def test_main_propagates_fetch_errors(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr("sys.argv", ["job_scraper"])

    def raise_fetch_error(url: str) -> str:
        raise RuntimeError("Request failed")

    monkeypatch.setattr(cli, "fetch_page", raise_fetch_error)

    with pytest.raises(RuntimeError, match="Request failed"):
        cli.main()
