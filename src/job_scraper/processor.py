
"""Data processing utilities for job listings."""


JOB_FIELDS = ("title", "company", "location", "url")
TEXT_FIELDS = ("title", "company", "location")


def process_job_listings(
    job_listings: list[dict[str, str]],
) -> list[dict[str, str]]:
    """Normalize job listing data."""
    processed_listings = []

    for job in job_listings:
        processed_job = {
            field: job.get(field, "").strip()
            for field in JOB_FIELDS
        }

        for field in TEXT_FIELDS:
            processed_job[field] = " ".join(
                processed_job[field].split()
            )

        processed_listings.append(processed_job)

    return processed_listings
