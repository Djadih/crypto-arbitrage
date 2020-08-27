import coinbase
import binance
import bitfinex

import asyncio
import time
import datetime


def main():

    # print("Coinbase price :", coinbase_price)
    # print("Binance price :", binance_price)

    highest_spread_percentage = 0

    while 1:
        prices = gather_prices()
        spread_percentage = print_statistics(prices)

        if highest_spread_percentage < spread_percentage:
            highest_spread_percentage = spread_percentage
            print("New highest spread percentage:", highest_spread_percentage, "%")
        else:
            print("Current highest spread percentage:", highest_spread_percentage, "%")

        print()

        time.sleep(.5)

def print_statistics(prices):

    # for exchange, price in prices.items():
    #     print(exchange, ":", price)

    coinbase_price = float(prices["coinbase"])
    binance_price = float(prices["binance"])
    bitfinex_price = float(prices["bitfinex"])

    spread = abs(coinbase_price - binance_price)

    coinbase_binance = round((spread / max(coinbase_price, binance_price)) * 100, 2)
    coinbase_bitfinex = round((spread / max(coinbase_price, bitfinex_price)) * 100, 2)
    binance_bitfinex = round((spread / max(binance_price, bitfinex_price)) * 100, 2)

    spread_percentage = max(coinbase_binance, coinbase_bitfinex, binance_bitfinex)

    print("Coinbase:", coinbase_price)
    print("Binance:", binance_price)
    print("Bitfinex:", bitfinex_price)
    print("Spread percentage:", spread_percentage, "%")

    if spread_percentage > (.3):
        with open('spreads', 'a') as file: 
            line = ("Spread_percentage: " + str(spread_percentage) + " . Coinbase: " + str(coinbase_price) + " Binance: " + str(binance_price) + " Bitfinex: " + str(bitfinex_price) + ". Time: " + str(datetime.datetime.now) + "\n")
            file.write(line)
    
    return spread_percentage



def gather_prices():

    prices = {}

    coinbase_price = coinbase.get_price()
    prices.update({"coinbase" : coinbase_price})
    
    binance_price = binance.get_price()
    prices.update({"binance" : binance_price})

    bitfinex_price = asyncio.run(bitfinex.get_price())
    prices.update({"bitfinex" : bitfinex_price})

    return prices


if __name__ == "__main__":
    main()