"""
Plotting functions
"""

import matplotlib.pyplot as plt


def plot_comparison(index_returns, portfolio_returns):
    """
    Plot index vs portfolio returns
    """
    plt.figure()
    plt.plot(index_returns, label="Index")
    plt.plot(portfolio_returns, label="Replicated Portfolio")
    plt.legend()
    plt.title("Index vs Replication")
    plt.xlabel("Time")
    plt.ylabel("Returns")
    plt.show()
