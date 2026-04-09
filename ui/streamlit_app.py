"""
Streamlit UI for Index Replication Engine
"""

import sys
import os
import streamlit as st
import pandas as pd

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data.loader import load_data
from utils.helpers import compute_returns
from models.optimizer import optimize_weights

st.title("📊 Index Replication Engine")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file, parse_dates=["Date"])
    df.set_index("Date", inplace=True)

    returns = compute_returns(df)

    index_returns = returns["Index"]
    stock_returns = returns.drop(columns=["Index"])

    weights = optimize_weights(stock_returns.values, index_returns.values)

    st.subheader("Optimal Weights")
    for stock, weight in zip(stock_returns.columns, weights):
        st.write(f"{stock}: {weight:.4f}")
