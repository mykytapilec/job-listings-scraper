
"""CSV export utilities for job listings."""

import csv
from pathlib import Path


CSV_FIELDS = ("title", "company", "location", "url")


def export_job_listings(
    job_listings: list[dict[str, str]],
    output_path: str | Path = "jobs.csv",
) -> None:
    """Export job listings to a CSV file."""
    file_path = Path(output_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    with file_path.open(
        mode="w",
        encoding="utf-8",
        newline="",
    ) as csv_file:
        writer = csv.DictWriter(
            csv_file,
            fieldnames=CSV_FIELDS,
            extrasaction="ignore",
        )

        writer.writeheader()
        writer.writerows(job_listings)
