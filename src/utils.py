#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""utils across project"""

import logging


def make_logger(name: str) -> logging.Logger:
    """Create a logger"""

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger
