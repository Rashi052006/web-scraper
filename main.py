from scraper import scrape_all_pages
from exporter import save_to_csv, save_to_json
URL = "https://books.toscrape.com/"


def main():
    books = scrape_all_pages(URL)
    print(f"Books scraped: {len(books)}")

    save_to_csv(books)
    save_to_json(books)


if __name__ == "__main__":
    main()