
"""Command-line interface for the job listings scraper."""

import argparse

from job_scraper.exporter import export_job_listings
from job_scraper.fetcher import fetch_page
from job_scraper.parser import DEFAULT_BASE_URL, parse_job_listings
from job_scraper.processor import process_job_listings


def create_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        description="Scrape job listings and export them to a CSV file.",
    )
    parser.add_argument(
        "--url",
        default=DEFAULT_BASE_URL,
        help="URL of the page containing job listings.",
    )
    parser.add_argument(
        "--output",
        default="jobs.csv",
        help="Path to the output CSV file.",
    )
    return parser


def main() -> None:
    """Run the job listings scraping pipeline."""
    parser = create_parser()
    args = parser.parse_args()

    html = fetch_page(args.url)
    job_listings = parse_job_listings(html, base_url=args.url)
    processed_listings = process_job_listings(job_listings)
    export_job_listings(processed_listings, args.output)

    print(f"Exported {len(processed_listings)} job listings to {args.output}")
