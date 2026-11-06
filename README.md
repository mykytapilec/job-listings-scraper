# Job Listings Scraper

A Python application for scraping job listings from web pages and exporting structured data to CSV.

## Features

- Fetch job listings from web pages.
- Parse HTML using BeautifulSoup.
- Extract job titles, company names, locations, and job URLs.
- Export job listings to CSV.
- Handle missing or incomplete data.

## Requirements

- Python 3.10+
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/mykytapilec/job-listings-scraper.git
cd job-listings-scraper
```

Create a virtual environment:

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Project Structure

```text
job-listings-scraper/
├── src/
│   └── job_scraper/
│       └── __init__.py
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## Usage

The application is currently under development.

## Testing

Run the test suite using:

```bash
pytest
```

## Technologies

- Python
- Requests
- BeautifulSoup4
- pytest
- CSV

## License

This project is intended for educational purposes.