#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Make decisions task"""

from trading_bot.utils import make_logger

LOGGER = make_logger(__name__)


def make_decisions():
    """make decisions"""

    LOGGER.info("I know which stocks to sell and which ones to buy")
