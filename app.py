import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px


# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Stock Market Data Analyzer",
    page_icon="📈",
    layout="wide"
)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📈 Stock Market Data Analyzer")

st.markdown("""
Analyze real-time stock market trends using:

- SMA20
- SMA50
- Volatility
- Daily Returns
- Volume Analysis
- Technical Trend Detection
""")


# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.header("📌 User Input")


ticker = st.sidebar.text_input(
    "Enter Stock Ticker",
    "AAPL"
)

start_date = st.sidebar.date_input(
    "Start Date"
)

end_date = st.sidebar.date_input(
    "End Date"
)

show_sma20 = st.sidebar.checkbox(
    "Show SMA 20",
    value=True
)

show_sma50 = st.sidebar.checkbox(
    "Show SMA 50",
    value=True
)

analyze_button = st.sidebar.button("Analyze Stock")


# ---------------------------------------------------
# DOWNLOAD DATA
# ---------------------------------------------------

if analyze_button:

    with st.spinner("Downloading stock data..."):

        df = yf.download(
            ticker,
            start=start_date,
            end=end_date
        )

    # ---------------------------------------------------
    # ERROR HANDLING
    # ---------------------------------------------------

    if df.empty:

        st.error("No stock data found!")

    else:

        # Fix multi-index issue
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)

        # Reset index
        df.reset_index(inplace=True)

        # ---------------------------------------------------
        # DATA CLEANING
        # ---------------------------------------------------

        df.dropna(inplace=True)

        # ---------------------------------------------------
        # CALCULATIONS
        # ---------------------------------------------------

        df['Daily Return'] = df['Close'].pct_change()

        df['SMA20'] = df['Close'].rolling(20).mean()

        df['SMA50'] = df['Close'].rolling(50).mean()

        volatility = df['Daily Return'].std()

        latest_close = df['Close'].values[-1]

        sma20_latest = df['SMA20'].values[-1]

        sma50_latest = df['SMA50'].values[-1]

        highest_price = df['High'].max()

        lowest_price = df['Low'].min()

        average_return = df['Daily Return'].mean()

        # ---------------------------------------------------
        # TREND ANALYSIS
        # ---------------------------------------------------

        if latest_close > sma50_latest:
            trend = "Bullish 📈"
        else:
            trend = "Bearish 📉"

        # ---------------------------------------------------
        # METRICS SECTION
        # ---------------------------------------------------

        st.subheader("📊 Market Summary")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "Current Price",
            f"${latest_close:.2f}"
        )

        col2.metric(
            "Highest Price",
            f"${highest_price:.2f}"
        )

        col3.metric(
            "Lowest Price",
            f"${lowest_price:.2f}"
        )

        col4.metric(
            "Trend",
            trend
        )

        # ---------------------------------------------------
        # SECOND ROW METRICS
        # ---------------------------------------------------

        col5, col6, col7 = st.columns(3)

        col5.metric(
            "Volatility",
            f"{volatility:.4f}"
        )

        col6.metric(
            "Average Daily Return",
            f"{average_return:.4f}"
        )

        col7.metric(
            "Volume",
            f"{df['Volume'].iloc[-1]:,.0f}"
        )

        # ---------------------------------------------------
        # STOCK PRICE CHART
        # ---------------------------------------------------

        st.subheader("📈 Stock Price Analysis")

        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                x=df['Date'],
                y=df['Close'],
                mode='lines',
                name='Close Price'
            )
        )

        # SMA20
        if show_sma20:

            fig.add_trace(
                go.Scatter(
                    x=df['Date'],
                    y=df['SMA20'],
                    mode='lines',
                    name='SMA 20'
                )
            )

        # SMA50
        if show_sma50:

            fig.add_trace(
                go.Scatter(
                    x=df['Date'],
                    y=df['SMA50'],
                    mode='lines',
                    name='SMA 50'
                )
            )

        fig.update_layout(
            title=f"{ticker} Stock Price Chart",
            xaxis_title="Date",
            yaxis_title="Price",
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ---------------------------------------------------
        # VOLUME ANALYSIS
        # ---------------------------------------------------

        st.subheader("📊 Volume Analysis")

        volume_fig = px.bar(
            df,
            x='Date',
            y='Volume',
            title="Trading Volume"
        )

        st.plotly_chart(
            volume_fig,
            use_container_width=True
        )

        # ---------------------------------------------------
        # DAILY RETURN DISTRIBUTION
        # ---------------------------------------------------

        st.subheader("📉 Daily Return Distribution")

        return_fig = px.histogram(
            df,
            x='Daily Return',
            nbins=50,
            title="Return Distribution"
        )

        st.plotly_chart(
            return_fig,
            use_container_width=True
        )

        # ---------------------------------------------------
        # TREND INTERPRETATION
        # ---------------------------------------------------

        st.subheader("🧠 AI-Style Insights")

        if latest_close > sma20_latest and latest_close > sma50_latest:

            st.success("""
            Strong bullish momentum detected.
            Current price is above SMA20 and SMA50.
            """)

        elif latest_close < sma20_latest and latest_close < sma50_latest:

            st.error("""
            Bearish trend detected.
            Current price is below SMA20 and SMA50.
            """)

        else:

            st.warning("""
            Sideways or uncertain trend detected.
            Market momentum is mixed.
            """)

        # ---------------------------------------------------
        # RISK ANALYSIS
        # ---------------------------------------------------

        st.subheader("⚠️ Risk Analysis")

        if volatility < 0.01:

            st.success("Low Volatility → Lower Risk Investment")

        elif volatility < 0.03:

            st.warning("Moderate Volatility → Medium Risk")

        else:

            st.error("High Volatility → High Risk Investment")

        # ---------------------------------------------------
        # RAW DATA
        # ---------------------------------------------------

        st.subheader("📄 Raw Stock Data")

        st.dataframe(df)

        # ---------------------------------------------------
        # DOWNLOAD CSV
        # ---------------------------------------------------

        csv = df.to_csv(index=False)

        st.download_button(
            label="📥 Download Processed CSV",
            data=csv,
            file_name=f"{ticker}_analysis.csv",
            mime='text/csv'
        )