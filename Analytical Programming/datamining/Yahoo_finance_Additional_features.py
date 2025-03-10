import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO

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
            ax.plot(df.index, df["Open"], label="Opening Price", linewidth=1, color="orange")
            ax.plot(df.index, df["Close"], label="Closing Price", linewidth=1, color="blue")
            ax.plot(df.index, df["High"], label="High Price", linewidth=1, color="green")
            ax.plot(df.index, df["Low"], label="Low Price", linewidth=1, color="red")
            ax.set_title(f"{selected_stock} Stock Prices")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (USD)")
            ax.legend()
            ax.grid()
            
            # Display plot
            st.pyplot(fig)
            
            # Export data as CSV
            csv_buffer = BytesIO()
            df.to_csv(csv_buffer, index=True)
            csv_buffer.seek(0)
            st.download_button(
                label="Download Data as CSV",
                data=csv_buffer,
                file_name=f"{stock_symbol}_stock_data.csv",
                mime="text/csv"
            )
    else:
        st.warning("Please select a valid start and end date.")
