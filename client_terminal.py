import requests
import time

API_URL = "https://yfinance-api-y9vd.onrender.com/stock/AAPL"

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()
        print("\n=== AAPL Stock Data ===")
        print(f"Name: {data['shortName']}")
        print(f"Price: {data['marketPrice']} {data['currency']}")
        print(f"High: {data['dayHigh']} | Low: {data['dayLow']}")
        print("========================")
    except Exception as e:
        print("Error fetching data:", e)
    time.sleep(5)
