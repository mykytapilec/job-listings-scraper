# Job Listings Scraper

A Python application that scrapes job listings from a website, processes the collected data, and exports it to a CSV file.

The project uses [Fake Jobs](https://realpython.github.io/fake-jobs/) as its default data source.

## Features

- Fetch job listing pages using HTTP requests.
- Parse job titles, company names, locations, and application URLs.
- Normalize extracted text and handle missing fields.
- Export job listings to CSV.
- Create output directories automatically.
- Configure the source URL and output path through CLI arguments.
- Run automated tests with pytest.

## Requirements

- Python 3.10 or higher
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/mykytapilec/job-listings-scraper.git
cd job-listings-scraper
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper with the default settings:

```bash
PYTHONPATH=src python -m job_scraper
```

By default, the application:

1. Fetches job listings from the Fake Jobs website.
2. Extracts job information.
3. Normalizes the collected data.
4. Exports the results to `jobs.csv` in the project root.

### Command-line arguments

| Argument | Description | Default |
|---|---|---|
| `--url` | URL of the page containing job listings | Fake Jobs URL |
| `--output` | Path to the output CSV file | `jobs.csv` |

Display available arguments:

```bash
PYTHONPATH=src python -m job_scraper --help
```

Use a custom source URL:

```bash
PYTHONPATH=src python -m job_scraper --url https://example.com/jobs
```

Specify a custom output path:

```bash
PYTHONPATH=src python -m job_scraper --output data/jobs.csv
```

Use both arguments:

```bash
PYTHONPATH=src python -m job_scraper \
  --url https://example.com/jobs \
  --output data/custom_jobs.csv
```

## CSV Output

The exported CSV file contains the following columns:

| Column | Description |
|---|---|
| `title` | Job title |
| `company` | Company name |
| `location` | Job location |
| `url` | Application page URL |

Example:

```csv
title,company,location,url
Senior Python Developer,Example Company,Warsaw,https://example.com/jobs/python-developer
```

The exporter uses UTF-8 encoding and creates missing parent directories automatically.

## Project Structure

```text
job-listings-scraper/
├── src/
│   └── job_scraper/
│       ├── __init__.py
│       ├── __main__.py
│       ├── cli.py
│       ├── exporter.py
│       ├── fetcher.py
│       ├── parser.py
│       └── processor.py
├── tests/
│   ├── test_cli.py
│   ├── test_exporter.py
│   ├── test_fetcher.py
│   ├── test_parser.py
│   └── test_processor.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Running Tests

Run the complete test suite:

```bash
PYTHONPATH=src pytest -v
```

## Dependencies

- [Requests](https://requests.readthedocs.io/) — HTTP requests.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) — HTML parsing.
- [pytest](https://docs.pytest.org/) — automated testing.

## Limitations

- The default data source is a demonstration website.
- The scraper depends on the HTML structure of the target website.
- Website structure changes may require updates to the parsing logic.
- The application currently processes one listing page per execution.

## License

No license has been specified yet.
