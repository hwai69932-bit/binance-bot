import time
import os
from binance.client import Client

api_key = os.getenv("API_KEY")
api_secret = os.getenv("API_SECRET")

client = Client(api_key, api_secret)

symbol = "BTCUSDT"
quantity = 0.001

while True:
    try:
        price = float(client.get_symbol_ticker(symbol=symbol)['price'])
        print(f"Current Price: {price}")

        if price % 2 == 0:
            print("BUY")
            order = client.order_market_buy(
                symbol=symbol,
                quantity=quantity
            )
