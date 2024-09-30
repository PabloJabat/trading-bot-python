#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""pull data"""
import os
import time
import concurrent.futures
from configparser import ConfigParser
from typing import List
from alpaca.trading.client import TradingClient
from alpaca.data import StockHistoricalDataClient, TimeFrameUnit, TimeFrame
from alpaca.data.requests import StockBarsRequest

config = ConfigParser()
a = config.read('config.ini')

trading_client = TradingClient(config["api"]["ApiKey"], config["api"]["ApiKey"], paper=True)
data_client = StockHistoricalDataClient(config["api"]["ApiKey"], config["api"]["ApiKey"])

ALL_ASSETS = trading_client.get_all_assets()
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
    request_params = StockBarsRequest(
        symbol_or_symbols=symbol,
        timeframe=TimeFrame(1, TimeFrameUnit.Day),
        limit=limit
    )

    data = data_client.get_stock_bars(request_params).df
    data.to_csv(f"data/{symbol}.csv")


def pull_symbols_data(symbols: List[str], limit: int) -> None:
    # NOTE: It seems that adding passing more parameters slows the runtime
    args = [(symbol, limit) for symbol in symbols]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: pull_symbol_data(*p), args)


if __name__ == "__main__":
    # needs to be run `python -m src.pull_data`
    # Apparently is too much data to be pulled if we want to get all the symbols
    # from a specific exchange index like NASDAQ.
    start = time.perf_counter()
    nasdaq_symbols = get_nasdaq_symbols()
    print(nasdaq_symbols)
    pull_symbol_data(nasdaq_symbols[1], limit=50)
    end = time.perf_counter()
    print(f"Pulled data in {end - start} secs")
