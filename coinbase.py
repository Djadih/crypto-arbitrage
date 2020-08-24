import cbpro
# import json

# public_client = cbpro.PublicClient()

# past_trades = public_client.get_product_trades(product_id='ETH-BTC')

# for trade in range(10):
#     print(next(past_trades))

# # print(next(past_trades))

def get_price():
    public_client = cbpro.PublicClient()
    response = public_client.get_product_ticker(product_id="ETH-USD")
    price = response["price"]

    return price

if __name__ == "__main__":
    print(get_price())