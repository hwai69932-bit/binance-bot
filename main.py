import time
import os
from binance.client import Client

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

client = Client(api_key, api_secret)

symbol = "BTCUSDT"

while True:
    try:
        ticker = client.get_symbol_ticker(symbol=symbol)
        price = float(ticker['price'])

        print(f"Current Price: {price}")

        if price < 50000:
            print("Price is low (TEST)")
        else:
            print("Price is high")

        time.sleep(5)

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
