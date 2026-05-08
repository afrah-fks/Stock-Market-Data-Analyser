# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os


# Create outputs folder
os.makedirs("outputs", exist_ok=True)


def plot_stock_price(df, ticker):

    plt.figure(figsize=(12, 6))

    plt.plot(df['Date'], df['Close'])

    plt.title(f"{ticker} Stock Price")

    plt.xlabel("Date")

    plt.ylabel("Close Price")

    plt.grid(True)

    plt.savefig(f"outputs/{ticker}_price_chart.png")

    plt.show()


def plot_moving_averages(df, ticker):

    plt.figure(figsize=(12, 6))

    plt.plot(df['Date'], df['Close'], label='Close Price')

    plt.plot(df['Date'], df['SMA_20'], label='SMA 20')

    plt.plot(df['Date'], df['SMA_50'], label='SMA 50')

    plt.title(f"{ticker} Moving Averages")

    plt.xlabel("Date")

    plt.ylabel("Price")

    plt.legend()

    plt.grid(True)

    plt.savefig(f"outputs/{ticker}_moving_average.png")

    plt.show()


def plot_return_distribution(df, ticker):

    plt.figure(figsize=(10, 5))

    sns.histplot(df['Daily Return'].dropna(), bins=50)

    plt.title(f"{ticker} Daily Return Distribution")

    plt.xlabel("Daily Return")

    plt.savefig(f"outputs/{ticker}_return_distribution.png")

    plt.show()