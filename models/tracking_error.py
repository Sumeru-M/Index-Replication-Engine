"""
Tracking error calculation
"""

import numpy as np


def calculate_tracking_error(index_returns, portfolio_returns):
    """
    Standard deviation of difference between index and portfolio returns
    """
    diff = index_returns - portfolio_returns
    return np.std(diff)
