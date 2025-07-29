from fastapi import FastAPI
from fastapi.responses import JSONResponse
import yfinance as yf

app = FastAPI()

@app.get("/stock/{ticker}")
async def get_stock_price(ticker: str):
    try:
        stock = yf.Ticker(ticker)
        data = stock.info
        return {
            "symbol": data.get("symbol"),
            "shortName": data.get("shortName"),
            "currency": data.get("currency"),
            "exchange": data.get("exchange"),
            "marketPrice": data.get("regularMarketPrice"),
            "previousClose": data.get("regularMarketPreviousClose"),
            "dayHigh": data.get("dayHigh"),
            "dayLow": data.get("dayLow")
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
