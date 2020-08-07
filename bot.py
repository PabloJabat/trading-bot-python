from moving_averages import *
from pull_data import get_nasdaq_symbols
import concurrent.futures


def make_decision(symbol: str):
    """
    This function returns what to do with a given symbol, buy, sell or do
    nothing.

    :param symbol:
    :return:
    """
    stock = load_symbol(symbol)["close"]
    fast_ma = compute_ma(stock, 10)
    slow_ma = compute_ma(stock, 40)
    if crossover(fast_ma, slow_ma):
        print(symbol)
        return 1
    elif crossover(slow_ma, fast_ma):
        return -1
    else:
        return 0


if __name__ == "__main__":
    nasdaq_symbols = get_nasdaq_symbols()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = list(executor.map(make_decision, nasdaq_symbols))
