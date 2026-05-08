# src/data_collection.py

import yfinance as yf
import pandas as pd
import os

def fetch_stock_data(ticker, start_date, end_date):
    """
    Fetch stock data using Yahoo Finance API
    """

    print(f"\nDownloading data for {ticker}...")

    df = yf.download(
        ticker,
        start=start_date,
        end=end_date
    )

    if df.empty:
        print("No data fetched!")
        return None

    # Fix multi-level columns issue
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    # Reset index
    df.reset_index(inplace=True)

    # Save CSV
    os.makedirs("data", exist_ok=True)

    file_path = f"data/{ticker}_stock_data.csv"

    df.to_csv(file_path, index=False)

    print(f"Data saved to {file_path}")

    return df


def load_csv_data(file_path):
    """
    Load stock data from CSV
    """

    if not os.path.exists(file_path):
        print("CSV file not found!")
        return None

    df = pd.read_csv(file_path)

    print("CSV data loaded successfully!")

    return df