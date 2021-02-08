#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Take actions task"""

from trading_bot.utils import make_logger

LOGGER = make_logger(__name__)


def take_actions():
    """Take actions"""
    LOGGER.info("I've bought and sold the required stocks")
