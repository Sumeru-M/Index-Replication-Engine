"""
Input validation
"""


def validate_dataframe(df):
    """
    Ensure dataframe has enough columns
    """
    if df.shape[1] < 2:
        raise ValueError("Dataset must include index and at least one stock")
