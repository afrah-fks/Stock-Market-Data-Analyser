# src/analysis.py

import pandas as pd
import numpy as np


def clean_data(df):
    """
    Clean stock data
    """

    print("\nCleaning data...")

    # Remove missing values
    df.dropna(inplace=True)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Reset index
    df.reset_index(drop=True, inplace=True)

    return df


def calculate_daily_returns(df):
   

    df['Daily Return'] = df['Close'].pct_change()

    return df


def calculate_moving_averages(df):
    """
    Calculate SMA indicators
    """

    df['SMA_20'] = df['Close'].rolling(window=20).mean()

    df['SMA_50'] = df['Close'].rolling(window=50).mean()

    return df


def calculate_volatility(df):
    """
    Calculate volatility
    """

    volatility = df['Daily Return'].std()

    return volatility


def highest_lowest_analysis(df):
    """
    Find highest and lowest stock prices
    """

    highest_price = df['High'].max()

    lowest_price = df['Low'].min()

    return highest_price, lowest_price


def trend_analysis(df):
    """
    Basic trend analysis
    """

    latest_close = df['Close'].values[-1]

    sma_50 = df['SMA_50'].values[-1]

    if latest_close > sma_50:
        trend = "Bullish"
    else:
        trend = "Bearish"

    return trend