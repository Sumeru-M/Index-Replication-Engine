"""
Main script to run index replication
"""

from data.loader import load_data
from utils.helpers import compute_returns
from utils.validators import validate_dataframe
from models.optimizer import optimize_weights
from models.tracking_error import calculate_tracking_error


def run():
    df = load_data("data/sample_prices.csv")

    validate_dataframe(df)

    returns = compute_returns(df)

    index_returns = returns["Index"]
    stock_returns = returns.drop(columns=["Index"])

    weights = optimize_weights(stock_returns.values, index_returns.values)

    portfolio_returns = stock_returns.values @ weights

    error = calculate_tracking_error(index_returns.values, portfolio_returns)

    print("Optimal Weights:", weights)
    print("Tracking Error:", error)


if __name__ == "__main__":
    run()
