import streamlit as st
import networkx as nx
import numpy as np
import pandas as pd

# Streamlit App: Lottery Predictor
# --------------------------------

# 1. Page configuration
st.set_page_config(page_title="🎯 Lottery Predictor", layout="centered")

st.title("🎯 Lottery Predictor")

# 2. Sidebar configuration
st.sidebar.header("Configuration")
num_picks = st.sidebar.number_input(
    "Numbers to pick", min_value=1, max_value=49, value=6, step=1
)
use_no_sequences = st.sidebar.checkbox(
    "Exclude sequential adjacency", value=True
)
use_parity = st.sidebar.checkbox(
    "Use parity grouping", value=True
)
use_decade = st.sidebar.checkbox(
    "Use decade clustering", value=True
)
use_digit_sum = st.sidebar.checkbox(
    "Use digital-sum similarity", value=False
)

# 3. Helper function for digital sum

def digital_sum(i: int) -> int:
    """
    Compute the sum of digits of i
    """
    return sum(int(c) for c in str(i))

# 4. Predict button
if st.sidebar.button("Predict"):
    # a) Build graph with selected biases
    G = nx.Graph()
    G.add_nodes_from(range(1, 50))
    for i in range(1, 50):
        for j in range(i + 1, 50):
            # Exclude sequential adjacency
            if use_no_sequences and abs(i - j) == 1:
                continue
            # Decade clustering
            if use_decade and (i - 1) // 10 == (j - 1) // 10:
                G.add_edge(i, j)
                continue
            # Parity grouping
            if use_parity and (i % 2) == (j % 2):
                G.add_edge(i, j)
                continue
            # Digital-sum similarity
            if use_digit_sum and digital_sum(i) == digital_sum(j):
                G.add_edge(i, j)

    # b) Compute degree-based weights
    degree_dict = dict(G.degree())
    total_degree = sum(degree_dict.values())
    weights = {node: count / total_degree for node, count in degree_dict.items()}

    # c) Perform the prediction
    numbers = np.array(list(weights.keys()))
    probs = np.array(list(weights.values()))
    probs /= probs.sum()
    # Draw without replacement
    picks = np.random.choice(numbers, size=int(num_picks), replace=False, p=probs)
    picks = sorted(picks)

    # 5. Display results
    st.subheader("Predicted Lottery Numbers")
    st.write(picks)

    # 6. Show weight distribution
    weight_df = pd.DataFrame({
        "Number": numbers,
        "Weight": probs
    }).sort_values("Weight", ascending=False)
    st.subheader("Top 5 Numbers by Weight")
    st.write(weight_df.head())
