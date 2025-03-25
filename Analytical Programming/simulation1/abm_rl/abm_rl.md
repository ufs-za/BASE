# Misinformation Dynamic Network Simulation

This readme contains the **spread and mitigation of misinformation** in a **scale-free network**. The simulation models **agents using Reinforcement Learning (RL)** to either **spread misinformation (Believers - Epsilon-Greedy)** or **counteract it (Skeptics - UCB)**.

## Features
- **Customizable Parameters**: Users can adjust the **number of agents, misinformation spread probability, fact-check probability, exploration rate (ε), and simulation steps**.
- **Scale-Free Network**: Built using the **Barabási–Albert preferential attachment model**, ensuring **realistic social network dynamics**.
- **Real-Time Visualization**:
  - **Network Graph**: Shows agent interactions and belief state changes.
  - **Time-Series Graphs**: Track the evolution of **Believers, Skeptics, and Neutrals** over time.
  - **Progress Updates**: Displays simulation progress and status updates.
- **Reinforcement Learning Mechanism**:
  - **Believers (Epsilon-Greedy)**: Optimize misinformation spread through **exploration-exploitation**.
  - **Skeptics (UCB - Upper Confidence Bound)**: Prioritize high-confidence fact-checking interventions.
  - **Rewards-Based Adaptation**: Tracks **cumulative rewards for both Believers and Skeptics**.

## Installation
To run the simulation locally, install the dependencies:

```sh
pip install streamlit networkx matplotlib numpy pandas
```

## Running the Simulation
Launch the Streamlit app using:

```sh
streamlit run app.py
```

## How It Works
1. **Customize parameters** using the sidebar sliders.
2. Click **Start Simulation** to begin the network evolution.
3. **The network and graphs update every 10 steps**, showing real-time interactions.
4. **Observe how misinformation spreads and how fact-checkers counteract it**.

## Visualizations
- **Scale-Free Network**: Displays agent interactions and belief states (Red = Believers, Blue = Skeptics, Gray = Neutrals, Green = Influencers).
- **Time-Series Graphs**:
  - **Believers vs. Skeptics Over Time**
  - **Neutral Count Over Time**
- **Confidence Intervals**: 95% confidence intervals are shaded for trend analysis.

## Model Assumptions
- **Influencers are high-impact nodes**, dynamically changing belief states.
- **Skeptics target high-confidence misinformation nodes**, while Believers explore randomly.
- **Once all Neutrals are converted**, misinformation spread **slows down** as Skeptics take over.

## Future Improvements
- **Multi-Agent RL Implementation** (e.g., Q-learning, Thompson Sampling for Believers)
- **Dynamic Network Evolution** (Nodes joining/leaving over time)
- **Agent-Based Visualization** (Animated agent movements within the network)

## Contributing
Feel free to submit **pull requests** for new features, optimizations, or additional RL strategies!

## License
This project is **open-source** under the **MIT License**.
