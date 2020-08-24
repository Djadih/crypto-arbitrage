import coinbase
import binance
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
            print("New highest spread percentage:", highest_spread_percentage)


        time.sleep(.5)

def print_statistics(prices):

    # for exchange, price in prices.items():
    #     print(exchange, ":", price)

    coinbase_price = float(prices["coinbase"])
    binance_price = float(prices["binance"])

    spread = abs(coinbase_price - binance_price)

    spread_percentage = (spread / max(coinbase_price, binance_price)) * 100

    print("Coinbase:", coinbase_price)
    print("Binance:", binance_price)
    print("Spread percentage:", spread_percentage, "\n")

    if spread_percentage > (.3):
        with open('spreads', 'a') as file: 
            line = ("Spread_percentage: " + str(spread_percentage) + " . Coinbase: " + str(coinbase_price) + " Binance: " + str(binance_price) + ". Time: " + str(datetime.datetime.now) + "\n")
            file.write(line)
    
    return spread_percentage



def gather_prices():

    prices = {}

    coinbase_price = coinbase.get_price()
    prices.update({"coinbase" : coinbase_price})
    
    binance_price = binance.get_price()
    prices.update({"binance" : binance_price})

    return prices


if __name__ == "__main__":
    main()