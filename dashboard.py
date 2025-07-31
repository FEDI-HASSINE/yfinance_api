import streamlit as st
import requests
import time
from datetime import datetime
import pandas as pd

st.set_page_config(page_title="📈 Stock Live Dashboard", layout="centered")

st.title("📈 Live Stock Price - AAPL")
placeholder = st.empty()

# Stock historical data
stock_prices = []

API_URL = "https://yfinance-api-y9vd.onrender.com/stock/AAPL"

while True:
    try:
        res = requests.get(API_URL)
        data = res.json()
        now = datetime.now().strftime("%H:%M:%S")
        price = data["marketPrice"]

        stock_prices.append({"time": now, "price": price})

        df = pd.DataFrame(stock_prices)

        with placeholder.container():
            st.line_chart(df.set_index("time"))

        time.sleep(5)

    except Exception as e:
        st.error(f"Erreur : {e}")
        time.sleep(5)
