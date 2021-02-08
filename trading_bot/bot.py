from moving_averages import *
from pull_data import get_nasdaq_symbols
import concurrent.futures
import pandas as pd
import datetime
import logging
import alpaca_trade_api
from config import API_KEY, SECRET_KEY


PAPER_TRADING_URL = "https://paper-api.alpaca.markets"
api = alpaca_trade_api.REST(API_KEY, SECRET_KEY, PAPER_TRADING_URL)
logging.basicConfig(level=logging.DEBUG)


def is_data_up_to_date(data: pd.DataFrame, offset: int) -> bool:
    """

    :param data:
    :param offset:
    :return:
    """
    return pd.to_datetime(
        data.index[-1]).date() == datetime.date.today() - datetime.timedelta(
        offset)


def load_close_data(symbols):
    """

    :param symbols:
    :return:
    """
    data = {}
    for symbol in symbols:
        data[symbol] = load_symbol(symbol)["close"]
    return data


def make_decision(stock: pd.Series):
    """
    This function returns what to do with a given symbol, buy, sell or do
    nothing.

    :param stock:
    :return:
    """
    fast_ma = compute_ma(stock, 10)
    slow_ma = compute_ma(stock, 40)
    if crossover(fast_ma, slow_ma):
        return 1
    elif crossover(slow_ma, fast_ma):
        return -1
    else:
        return 0


if __name__ == "__main__":
    # We need to add a check for weekends.
    if datetime.date.weekday(datetime.date.today()) > 4:
        raise Exception("Market is closed")

    # Load the data and check that is up to date
    nasdaq_symbols = get_nasdaq_symbols()[:200]
    data = load_close_data(nasdaq_symbols)

    # Filter out the symbols that aren´t up to date
    count_deleted = 0
    if not all([is_data_up_to_date(stock, 3) for stock in data.values()]):
        logging.debug("Some symbols aren´t up to date")
        for symbol in list(data):
            if is_data_up_to_date(data[symbol], 3):
                count_deleted += 1
                del data[symbol]
                nasdaq_symbols.remove(symbol)
    logging.debug(f"Deleted {count_deleted} symbol(s)")

    # Run the decision making algorithm
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(make_decision, data.values())

    # Processing the decisions
    decisions = zip(nasdaq_symbols, results)

    stock_to_buy = [symbol for symbol, decision in decisions if decision == 1]
    stock_to_sell = [symbol for symbol, decision in decisions if decision == 1]

    logging.debug(f"Found {len(stock_to_buy)} stock(s) to buy")
    logging.debug(f"Found {len(stock_to_sell)} stock(s) to sell")

    for position in api.list_positions():
        if position.symbol in stock_to_sell:
            _ = api.submit_order(
                position.symnol,
                qty=position.qty,
                side="sell",
                type="market",
                time_in_force="gtc"
            )

    for symbol in stock_to_buy:
        _ = api.submit_order(
            symbol,
            qty=1,
            side="buy",
            type="market",
            time_in_force="gtc"
        )
        logging.debug(f"Bought {symbol} stock(s)")
