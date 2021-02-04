import time
import concurrent.futures
from .config import *
from typing import List
import alpaca_trade_api

BASE_URL = "https://paper-api.alpaca.markets"
BARS_URL = f"https://data.alpaca.markets/v1/bars"
HEADERS = {
    "APCA-API-KEY-ID": API_KEY,
    "APCA-API-SECRET-KEY": SECRET_KEY
}

market_api = alpaca_trade_api.REST(API_KEY, SECRET_KEY, BASE_URL)
bars_api = alpaca_trade_api.REST(API_KEY, SECRET_KEY)

ALL_ASSETS = market_api.list_assets()
ALL_ACTIVE_ASSETS = list(filter(lambda x: x.status == "active", ALL_ASSETS))
ALL_INACTIVE_ASSETS = list(
    filter(lambda x: x.status == "inactive", ALL_ASSETS))

assert len(ALL_INACTIVE_ASSETS) + len(ALL_ACTIVE_ASSETS) == len(ALL_ASSETS)


def get_available_exchanges():
    exchanges = set()
    for asset in ALL_ASSETS:
        exchanges.add(asset.exchange)
    return exchanges


def get_assets_from(exchange, inactive=True) -> List[str]:
    exchanges = get_available_exchanges()
    if exchange not in exchanges:
        for index in exchanges:
            print(index)
        raise Exception("Invalid exchange")
    else:
        if inactive:
            assets = ALL_ASSETS
        else:
            assets = ALL_ACTIVE_ASSETS

        return list(map(lambda asset: asset.symbol,
                        filter(lambda asset: asset.exchange == exchange,
                               assets)))


def get_nasdaq_symbols(inactive=True) -> List[str]:
    return get_assets_from("NASDAQ", inactive=inactive)


def pull_symbol_data(symbol: str, limit: int) -> None:
    data = bars_api.get_barset(symbol, "1D", limit=limit).df
    data.to_csv(f"data/{symbol}.csv")


def pull_symbols_data(symbols: List[str], limit: int) -> None:
    # NOTE: It seems that adding passing more parameters slows the runtime
    args = [(symbol, limit) for symbol in symbols]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: pull_symbol_data(*p), args)


if __name__ == "__main__":
    # Apparently is too much data to be pulled if we want to get all the symbols
    # from a specific exchange index like NASDAQ.
    start = time.perf_counter()
    nasdaq_symbols = get_nasdaq_symbols()
    pull_symbols_data(nasdaq_symbols[:200], limit=50)
    end = time.perf_counter()
    print(f"Pulled data in {round(end - start, 2)} secs")
