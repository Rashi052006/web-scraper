import logging
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"

logging.basicConfig(
    filename="logs/scraper.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def fetch_page(url, retries=3):
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()

            logging.info(
                f"Successfully fetched: {url}"
            )

            return response.text

        except requests.RequestException as error:
            logging.warning(
                f"Attempt {attempt}/{retries} failed for {url}: {error}"
            )

    logging.error(
        f"Failed to fetch {url} after {retries} attempts."
    )

    return None


def parse_books(html):
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    books = []

    for book in soup.select("article.product_pod"):
        try:
            title = book.h3.a["title"]
            price = book.select_one(".price_color").text.strip()
            availability = book.select_one(".availability").text.strip()

            rating_element = book.select_one("p.star-rating")
            rating = (
                rating_element.get("class")[1]
                if rating_element
                else "Unknown"
            )

            relative_url = book.h3.a["href"]
            product_url = urljoin(BASE_URL, relative_url)

            books.append({
                "title": title,
                "price": price,
                "rating": rating,
                "availability": availability,
                "product_url": product_url
            })

        except (AttributeError, KeyError, TypeError) as error:
            logging.warning(f"Could not parse a book: {error}")

    return books


def scrape_all_pages(start_url=BASE_URL):
    all_books = []
    current_url = start_url
    page_number = 1

    while current_url:
        print(f"Scraping page {page_number}...")
        time.sleep(1)

        html = fetch_page(current_url)

        if html is None:
            logging.error(
                f"Skipping page {page_number} because it could not be fetched."
            )
            current_url = None
            continue

        books = parse_books(html)
        all_books.extend(books)

        logging.info(
            f"Page {page_number}: {len(books)} books extracted."
        )

        soup = BeautifulSoup(html, "html.parser")
        next_button = soup.select_one("li.next a")

        if next_button:
            current_url = urljoin(
                current_url,
                next_button["href"]
            )
            page_number += 1
        else:
            current_url = None

    logging.info(
        f"Scraping completed. Total books: {len(all_books)}"
    )

    return all_books


if __name__ == "__main__":
    books = scrape_all_pages()

    print(f"\nTotal books scraped: {len(books)}")