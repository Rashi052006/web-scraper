import pandas as pd


FILE_PATH = "data/books.csv"


def validate_data():
    df = pd.read_csv(FILE_PATH)

    print("\n========== DATA QUALITY REPORT ==========")

    print(f"Total records: {len(df)}")

    duplicate_urls = df["product_url"].duplicated().sum()
    print(f"Duplicate URLs: {duplicate_urls}")

    missing_values = df.isnull().sum()
    print("\nMissing values:")
    print(missing_values)

    invalid_prices = (df["price"] <= 0).sum()
    print(f"\nInvalid prices: {invalid_prices}")

    invalid_ratings = (
        (df["rating"] < 1) |
        (df["rating"] > 5)
    ).sum()

    print(f"Invalid ratings: {invalid_ratings}")

    print("\nPrice statistics:")
    print(df["price"].describe())

    print("\nRating distribution:")
    print(df["rating"].value_counts().sort_index())

    print("\n========== VALIDATION COMPLETE ==========")


if __name__ == "__main__":
    validate_data()