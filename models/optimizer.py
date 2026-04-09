"""
Portfolio optimization to replicate index
"""

import numpy as np
from scipy.optimize import minimize


def optimize_weights(stock_returns, index_returns):
    """
    Find weights that minimize tracking error
    """

    num_assets = stock_returns.shape[1]

    # Initial guess: equal weights
    initial_weights = np.ones(num_assets) / num_assets

    # Constraint: weights sum to 1
    constraints = ({'type': 'eq', 'fun': lambda w: np.sum(w) - 1})

    # Bounds: weights between 0 and 1
    bounds = [(0, 1)] * num_assets

    def objective(weights):
        portfolio_returns = np.dot(stock_returns, weights)
        diff = index_returns - portfolio_returns
        return np.std(diff)

    result = minimize(objective, initial_weights, bounds=bounds, constraints=constraints)

    return result.x
