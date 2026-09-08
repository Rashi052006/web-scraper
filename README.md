Web Scraper

A Python-based web scraping project that extracts book information from "Books to Scrape" (https://books.toscrape.com/), cleans and validates the collected data, and exports it into CSV and JSON formats.

📌 Project Overview

This project demonstrates how Python can be used to collect structured information from a website efficiently.

The scraper navigates through all available pages on the website and extracts details such as:

- Book title
- Price
- Availability
- Rating
- Product URL

The collected information is then cleaned, validated, and saved in both CSV and JSON formats.

🎯 Objective

The main objective of this project is to build an intermediate-level web scraper using Python while implementing practical concepts such as:

- HTTP requests
- HTML parsing
- Pagination
- Data cleaning
- Data validation
- Error handling
- Retry mechanisms
- Logging
- CSV and JSON data export

🛠️ Technologies Used

- Python 3.11
- Requests – for sending HTTP requests
- BeautifulSoup – for parsing HTML
- Pandas – for data cleaning and processing
- JSON – for structured data export
- Git & GitHub – for version control and project hosting

✨ Features

1. Web Scraping

Fetches book information from the Books to Scrape website using Python.

2. Pagination

Automatically navigates through all available pages instead of scraping only the first page.

3. Data Extraction

Extracts:

- Title
- Price
- Availability
- Rating
- Product URL

4. Retry Mechanism

If a page request fails, the scraper automatically retries the request up to three times.

5. Request Timeout

A timeout is configured for HTTP requests to prevent the scraper from waiting indefinitely.

6. Polite Scraping

A short delay is added between page requests to reduce unnecessary load on the website.

7. Logging

Scraping activity and request failures are recorded in a log file.

8. Data Cleaning

The collected data is cleaned using Pandas before being exported.

9. Data Validation

The project checks for:

- Duplicate product URLs
- Missing values
- Invalid prices
- Invalid ratings

10. Multiple Export Formats

The final dataset is exported to:

- CSV
- JSON

📊 Results

The scraper successfully collected data for 1,000 books across 50 pages.

The validation process confirmed:

- Total records: 1,000
- Duplicate URLs: 0
- Missing values: 0
- Invalid prices: 0
- Invalid ratings: 0

📂 Project Structure

web-scraper/
│
├── data/
│   ├── books.csv
│   └── books.json
│
├── logs/
│   └── scraper.log
│
├── venv/
│
├── main.py
├── scraper.py
├── exporter.py
├── validate_data.py
├── requirements.txt
├── .gitignore
└── README.md

«Note: "venv/" and "logs/" are excluded from Git using ".gitignore".»

⚙️ Installation

1. Clone the repository

git clone <your-github-repository-url>
cd web-scraper

2. Create a virtual environment

python -m venv venv

3. Activate the virtual environment

Windows PowerShell:

venv\Scripts\Activate.ps1

4. Install dependencies

pip install -r requirements.txt

▶️ How to Run

Run the scraper:

python main.py

The scraped data will be saved in:

data/books.csv
data/books.json

To validate the collected data:

python validate_data.py

🔍 Data Validation

The validation script generates a data quality report containing:

- Record count
- Duplicate URL count
- Missing values
- Invalid prices
- Invalid ratings
- Price statistics
- Rating distribution

📝 Ethical Scraping

This project uses Books to Scrape, a website specifically designed for practicing web scraping.

When scraping websites in real-world applications, always respect:

- "robots.txt"
- Website terms of service
- Rate limits
- Server resources
- Applicable laws and regulations

👩‍💻 Author

Rashi

BCA Graduate | Python | Data Analytics | Web Scraping

---

⭐ This project was developed as part of a Python Programming Internship project.
