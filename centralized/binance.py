import requests
import json

#print(requests.get("https://api.binance.com/api/v3/trades", {"symbol":"ETHBTC", "limit" : 1}).text)
# print(requests.get("https://api.binance.com/api/v3/ticker/price", {"symbol":"ETHBTC"}).text)

def get_price():
    response = requests.get("https://api.binance.com/api/v3/ticker/price", {"symbol":"ETHUSDT"}).json()
    price = response["price"]

    return price
