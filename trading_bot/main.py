from pull_data import get_nasdaq_symbols, pull_symbols_data

symbols = get_nasdaq_symbols()

pull_symbols_data(symbols[:10], 5)