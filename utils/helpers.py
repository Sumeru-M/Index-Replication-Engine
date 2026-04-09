"""
Helper functions
"""

import pandas as pd


def compute_returns(price_df):
    """
    Convert prices to returns
    """
    return price_df.pct_change().dropna()
