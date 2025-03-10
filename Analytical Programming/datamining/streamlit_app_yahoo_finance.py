import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

# Dictionary of stock symbols
STOCKS = {
    "Alphabet (GOOGL)": "GOOGL",
    "Nvidia (NVDA)": "NVDA",
    "Microsoft (MSFT)": "MSFT"
}

# Streamlit UI
st.title("Stock Time Series Visualization")

# Select a stock
selected_stock = st.selectbox("Choose a stock:", list(STOCKS.keys()))

# Select date range
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

# Fetch data button
if st.button("Fetch Data"):
    if start_date and end_date:
        stock_symbol = STOCKS[selected_stock]

        # Download stock data
        df = yf.download(stock_symbol, start=start_date, end=end_date)

        if df.empty:
            st.warning("No data available for the selected date range. Try another period.")
        else:
            # Plot the time series data
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(df.index, df["Close"], label="Closing Price", color="blue")
            ax.set_title(f"{selected_stock} Stock Prices")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (USD)")
            ax.legend()
            ax.grid()

            # Display plot
            st.pyplot(fig)
    else:
        st.warning("Please select a valid start and end date.")
