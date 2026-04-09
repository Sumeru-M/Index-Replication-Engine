"""
Load price data
"""

import pandas as pd


def load_data(filepath):
    """
    Load CSV file containing price data.

    Expected format:
    Date | Index | Stock1 | Stock2 | ...
    """
    df = pd.read_csv(filepath, parse_dates=["Date"])
    df.set_index("Date", inplace=True)
    return df
