import sys
from config import *
from typing import List
import alpaca_trade_api as tradeapi


BARS_URL = f"https://data.alpaca.markets/v1/bars"
HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}


def pull_symbols_data(symbols: List[str], limit: int) -> None:
    api = tradeapi.REST(API_KEY, SECRET_KEY)
    for symbol in symbols:
        data = api.get_barset(symbol, "1D", limit=limit).df
        data.to_csv(f"data/{symbol}.csv")


if __name__ == "__main__":
    pull_symbols_data(sys.argv[1:], 5)
