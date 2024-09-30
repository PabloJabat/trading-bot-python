#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Load data task"""

from src.utils import make_logger

LOGGER = make_logger(__name__)


def load_data():
    """function to pull the data for the trading bot
    """

    LOGGER.info("Starting to load available symbols")
    # symbols = get_nasdaq_symbols()
    # some_symbols = symbols[:10]
    LOGGER.info("Starting to pull symbols data")
    # pull_symbols_data(some_symbols, 10)
    LOGGER.info("finshed pulling data")
