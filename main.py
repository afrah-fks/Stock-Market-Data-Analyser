# main.py

from src.data_collection import fetch_stock_data
from src.analysis import (
    clean_data,
    calculate_daily_returns,
    calculate_moving_averages,
    calculate_volatility,
    highest_lowest_analysis,
    trend_analysis
)

from src.visualization import (
    plot_stock_price,
    plot_moving_averages,
    plot_return_distribution
)

from src.report_generator import generate_report


# User input
ticker = input("Enter Stock Ticker: ")

start_date = input("Enter Start Date (YYYY-MM-DD): ")

end_date = input("Enter End Date (YYYY-MM-DD): ")


# Fetch stock data
df = fetch_stock_data(
    ticker,
    start_date,
    end_date
)

# Clean data
df = clean_data(df)

# Calculations
df = calculate_daily_returns(df)

df = calculate_moving_averages(df)

volatility = calculate_volatility(df)

highest_price, lowest_price = highest_lowest_analysis(df)

trend = trend_analysis(df)

# Visualizations
plot_stock_price(df, ticker)

plot_moving_averages(df, ticker)

plot_return_distribution(df, ticker)

# Generate report
generate_report(
    ticker,
    volatility,
    highest_price,
    lowest_price,
    trend
)

print("\nAnalysis Completed Successfully!")