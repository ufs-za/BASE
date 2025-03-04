import streamlit as st
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Title of the App
st.title("A/B Testing Click Demo")
st.write("Click to simulate user actions and compare two versions (A & B).")

# Initialize session state
if "clicks_A" not in st.session_state:
    st.session_state.clicks_A = 0
    st.session_state.clicks_B = 0
    st.session_state.visitors_A = 0
    st.session_state.visitors_B = 0

# User Click Simulation
st.subheader("Click Simulation")
col1, col2 = st.columns(2)

with col1:
    if st.button("Click Version A"):
        st.session_state.clicks_A += 1
    st.session_state.visitors_A += 1
    st.write(f"Clicks: {st.session_state.clicks_A}")
    st.write(f"Visitors: {st.session_state.visitors_A}")

with col2:
    if st.button("Click Version B"):
        st.session_state.clicks_B += 1
    st.session_state.visitors_B += 1
    st.write(f"Clicks: {st.session_state.clicks_B}")
    st.write(f"Visitors: {st.session_state.visitors_B}")

# Compute conversion rates
rate_A = st.session_state.clicks_A / max(1, st.session_state.visitors_A)
rate_B = st.session_state.clicks_B / max(1, st.session_state.visitors_B)

def evaluate_ab_test(n_A, conv_A, n_B, conv_B):
    # Perform a two-proportion z-test
    p_A = conv_A / max(1, n_A)
    p_B = conv_B / max(1, n_B)
    p_pool = (conv_A + conv_B) / max(1, n_A + n_B)
    se = np.sqrt(p_pool * (1 - p_pool) * (1/max(1, n_A) + 1/max(1, n_B)))
    z_score = (p_B - p_A) / max(1e-6, se)
    p_value = 1 - stats.norm.cdf(z_score)  # One-tailed test
    return p_A, p_B, z_score, p_value

# Perform A/B Test Analysis
p_A, p_B, z_score, p_value = evaluate_ab_test(
    st.session_state.visitors_A, st.session_state.clicks_A, 
    st.session_state.visitors_B, st.session_state.clicks_B
)

# Display Results
st.subheader("Results")
st.write(f"**Conversion Rate for A:** {p_A:.2%}")
st.write(f"**Conversion Rate for B:** {p_B:.2%}")
st.write(f"**Z-Score:** {z_score:.2f}")
st.write(f"**P-Value:** {p_value:.4f}")

# Interpretation
st.subheader("Conclusion")
if p_value < 0.05:
    st.success("Version B performs significantly better than Version A! ✅")
else:
    st.warning("No significant difference between A and B. Keep testing!")

# Visualization
fig, ax = plt.subplots()
bars = ax.bar(["Version A", "Version B"], [p_A, p_B], color=['blue', 'red'])
ax.bar_label(bars, fmt='%.2f%%')
ax.set_ylabel("Conversion Rate")
st.pyplot(fig)
