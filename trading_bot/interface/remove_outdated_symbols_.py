#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Load data task"""


from trading_bot.utils import make_logger

LOGGER = make_logger(__name__)


def remove_outdated_symbols():
    """Remove outdated symbols"""

    LOGGER.info("I've removed the symbols info which is outdated")
