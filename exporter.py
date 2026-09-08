import pandas as pd
import json


def clean_data(books):
    df = pd.DataFrame(books)

    if df.empty:
        return df

    # Remove duplicate books
    df.drop_duplicates(subset=["product_url"], inplace=True)

    # Clean text fields
    df["title"] = df["title"].str.strip()
    df["availability"] = df["availability"].str.strip()

    # Convert price from £51.77 to 51.77
    df["price"] = (
    df["price"]
    .str.replace(r"[^0-9.]", "", regex=True)
)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Make rating values consistent
    rating_map = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }

    df["rating"] = df["rating"].map(rating_map)

    # Replace missing values
    df["availability"] = df["availability"].fillna("Unknown")
    df["rating"] = df["rating"].fillna(0)

    return df


def save_to_csv(books, filename="data/books.csv"):
    df = clean_data(books)

    df.to_csv(filename, index=False, encoding="utf-8")

    print(f"CSV file saved successfully: {filename}")


def save_to_json(books, filename="data/books.json"):
    df = clean_data(books)

    df.to_json(
        filename,
        orient="records",
        indent=4,
        force_ascii=False
    )

    print(f"JSON file saved successfully: {filename}")