import asyncio
from bfxapi import Client

async def get_price():
    bfx = Client()
    ticker = await bfx.rest.get_public_ticker('tETHUSD')

    # price is the 6th element of the ticker array
    # https://github.com/bitfinexcom/bitfinex-api-py/blob/729019b4c492a822d7074a8d21e274a3fbc6fab7/bfxapi/rest/bfx_rest.py#L152

    return round(ticker[6], 2)

# async def run():
#     # ticker = await get_price()
#     ticker = await get_price()

#     print(ticker)

    # return(ticker[6])

# if __name__ == "__main__":
#     asyncio.run(main())

# t = asyncio.ensure_future(run())
# asyncio.get_event_loop().run_until_complete(t)