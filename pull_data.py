import time
import requests
import bs4
import concurrent.futures
from config import *
from typing import List
import alpaca_trade_api as tradeapi


BARS_URL = f"https://data.alpaca.markets/v1/bars"
HEADERS = {"APCA-API-KEY-ID": API_KEY, "APCA-API-SECRET-KEY": SECRET_KEY}


def get_nasquad_symbols() -> List[str]:
    url = "https://es.wikipedia.org/wiki/NASDAQ-100"
    resp = requests.get(url)
    soup = bs4.BeautifulSoup(resp.text, features="lxml")

    table = soup.find("table", {"class": "wikitable sortable"})

    symbols_col = []
    for row in table.findAll("tr")[1:]:
        symbols_col.append(row.findAll("td")[0].text)

    symbols = []
    for symbol in symbols_col:
        symbols.append(symbol.split(",")[0].strip())

    return symbols


def pull_symbol_data(symbol: str, limit: int) -> None:
    api = tradeapi.REST(API_KEY, SECRET_KEY)
    data = api.get_barset(symbol, "1D", limit=limit).df
    data.to_csv(f"data/{symbol}.csv")


def pull_symbols_data(symbols: List[str], limit: int) -> None:
    # NOTE: It seems that adding passing more parameters slows the runtime
    args = [(symbol, limit) for symbol in symbols]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(lambda p: pull_symbol_data(*p), args)


if __name__ == "__main__":
    start = time.perf_counter()
    nasquad_symbols = get_nasquad_symbols()
    pull_symbols_data(nasquad_symbols, limit=5)
    end = time.perf_counter()
    print(f"Pulled data in {round(end - start, 2)} secs")
