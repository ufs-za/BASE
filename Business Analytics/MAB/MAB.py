import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

# Title of the App
st.title("Multi-Armed Bandit: Epsilon-Greedy, Thompson Sampling, and UCB")
st.write("Click to simulate user actions on different advertisements and let different algorithms dynamically learn which advert (1, 2, 3, or 4) is better.")

# Parameters
EPSILON = 0.1  # Exploration rate for Epsilon-Greedy
ALPHA, BETA = 1, 1  # Parameters for Thompson Sampling
C = 2  # Exploration factor for UCB

# Initialize session state for MAB
if "rewards" not in st.session_state:
    st.session_state.rewards = {"Ad1": 0, "Ad2": 0, "Ad3": 0, "Ad4": 0}
    st.session_state.clicks = {"Ad1": 0, "Ad2": 0, "Ad3": 0, "Ad4": 0}
    st.session_state.alpha = {"Ad1": ALPHA, "Ad2": ALPHA, "Ad3": ALPHA, "Ad4": ALPHA}
    st.session_state.beta = {"Ad1": BETA, "Ad2": BETA, "Ad3": BETA, "Ad4": BETA}
    st.session_state.total_visitors = 0  # Shared visitor pool

# Simulate a visitor arriving
st.session_state.total_visitors += 1

# Choose action based on epsilon-greedy strategy
def choose_action_epsilon_greedy():
    if np.random.rand() < EPSILON:
        return np.random.choice(["Ad1", "Ad2", "Ad3", "Ad4"])  # Explore
    else:
        return max(st.session_state.rewards, key=lambda k: st.session_state.rewards[k] / max(1, st.session_state.clicks[k]))

# Choose action based on Upper Confidence Bound (UCB)
def choose_action_ucb():
    total_visits = st.session_state.total_visitors
    ucb_values = {ad: (st.session_state.rewards[ad] / max(1, st.session_state.clicks[ad])) + C * np.sqrt(np.log(total_visits) / max(1, st.session_state.clicks[ad])) for ad in st.session_state.rewards}
    return max(ucb_values, key=ucb_values.get)

# Choose action based on Thompson Sampling
def choose_action_thompson():
    samples = {ad: np.random.beta(st.session_state.alpha[ad], st.session_state.beta[ad]) for ad in st.session_state.rewards}
    return max(samples, key=samples.get)

# User Click Simulation
st.subheader("Advert Click Simulation")
cols = st.columns(4)
for idx, ad in enumerate(["Ad1", "Ad2", "Ad3", "Ad4"]):
    with cols[idx]:
        if st.button(f"Click Advert {idx+1}"):
            st.session_state.clicks[ad] += 1
            st.session_state.rewards[ad] += np.random.choice([0, 1], p=[0.5, 0.5])
            st.session_state.alpha[ad] += 1 if st.session_state.rewards[ad] > 0 else 0  # Update for Thompson Sampling
            st.session_state.beta[ad] += 1 if st.session_state.rewards[ad] == 0 else 0  # Update for Thompson Sampling
        st.write(f"Clicks: {st.session_state.clicks[ad]}")
        st.write(f"Conversions: {st.session_state.rewards[ad]}")
        st.write(f"Total Visitors: {st.session_state.total_visitors}")

# Compute estimated conversion rates
conversion_rates = {ad: st.session_state.rewards[ad] / max(1, st.session_state.clicks[ad]) for ad in st.session_state.rewards}

# Display Results
st.subheader("Results")
for ad, rate in conversion_rates.items():
    st.write(f"**Estimated Conversion Rate for {ad}:** {rate:.2%}")

# Decision Making using MAB strategies
epsilon_choice = choose_action_epsilon_greedy()
ucb_choice = choose_action_ucb()
thompson_choice = choose_action_thompson()

# Interpretation
st.subheader("Conclusion")
if st.session_state.total_visitors < 30:
    st.info("📊 More data is needed to determine a clear winner. Keep testing!")
st.success(f"🚀 **Epsilon-Greedy prefers:** {epsilon_choice}")
st.success(f"🚀 **UCB prefers:** {ucb_choice}")
st.success(f"🚀 **Thompson Sampling prefers:** {thompson_choice}")

# Visualization
fig, ax = plt.subplots()
bars = ax.bar(["Ad1", "Ad2", "Ad3", "Ad4"], [conversion_rates["Ad1"], conversion_rates["Ad2"], conversion_rates["Ad3"], conversion_rates["Ad4"]], color=['blue', 'red', 'green', 'purple'])
ax.bar_label(bars, fmt='%.2f%%')
ax.set_ylabel("Estimated Conversion Rate")
st.pyplot(fig)
