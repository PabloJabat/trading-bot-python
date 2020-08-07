import pandas as pd
from pathlib import WindowsPath
from typing import Sequence
from numbers import Number


def load_symbol(symbol: str) -> pd.DataFrame:
    data_path = WindowsPath("data")
    return pd.read_csv(data_path / f"{symbol}.csv", header=1, index_col=0)


def compute_ma(data, window: int):
    ma = data.rolling(window=window).mean()
    return ma


def crossover(series1: Sequence, series2: Sequence) -> bool:
    """
    Return `True` if `series1` just crossed over
    `series2`.
    """
    series1 = (
        series1.values if isinstance(series1, pd.Series) else
        (series1, series1) if isinstance(series1, Number) else
        series1)
    series2 = (
        series2.values if isinstance(series2, pd.Series) else
        (series2, series2) if isinstance(series2, Number) else
        series2)
    try:
        return series1[-2] < series2[-2] and series1[-1] > series2[-1]
    except IndexError:
        return False
