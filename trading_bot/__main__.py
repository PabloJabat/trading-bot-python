#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point"""

from pull_data import get_nasdaq_symbols, pull_symbols_data

symbols = get_nasdaq_symbols()

pull_symbols_data(symbols[:10], 5)
