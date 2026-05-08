# src/report_generator.py

import os


def generate_report(
    ticker,
    volatility,
    highest_price,
    lowest_price,
    trend
):

    os.makedirs("reports", exist_ok=True)

    report_path = f"reports/{ticker}_report.txt"

    with open(report_path, "w") as file:

        file.write("STOCK MARKET ANALYSIS REPORT\n")
        file.write("=" * 40 + "\n\n")

        file.write(f"Stock Ticker: {ticker}\n")
        file.write(f"Trend: {trend}\n")
        file.write(f"Volatility: {volatility:.4f}\n")
        file.write(f"Highest Price: {highest_price:.2f}\n")
        file.write(f"Lowest Price: {lowest_price:.2f}\n")

        file.write("\nAnalysis Summary:\n")

        if trend == "Bullish":
            file.write("Stock shows upward momentum.\n")
        else:
            file.write("Stock shows downward trend.\n")

    print(f"\nReport saved at: {report_path}")