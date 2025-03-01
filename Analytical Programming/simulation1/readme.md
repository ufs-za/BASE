# Scale-Free Network Disease Spread Simulation

## Overview
This Python script implements a **Scale-Free Network Disease Spread Simulation** using **Streamlit** for interactivity and **NetworkX** for network modeling. The simulation models the spread of an infection across a network, tracking the number of infections, recoveries, and deaths over time.

## Key Features
- **Scale-Free Network:** The network follows a Barabási-Albert model, ensuring that some nodes (hubs) have significantly more connections than others.
- **Interactive Parameters:** Users can adjust:
  - Number of agents (nodes)
  - Initial number of infected individuals
  - Probability of infection spread
  - Duration of the simulation (time steps)
- **Agent-Based Model:** Each node represents an individual with:
  - A **status** (`susceptible`, `infected`, `alive`, `dead`)
  - A **size** that determines susceptibility to infection
- **Disease Progression Rules:**
  - **Infection Spread:** Infected nodes can spread the disease to susceptible neighbors based on their size (larger nodes take longer to infect smaller ones).
  - **Recovery Mechanism:** After being infected for 3 time steps, a node either **recovers (turns green)** or **dies (turns blue)** with a 50% probability.
  - **Time Series Tracking:** Infection, recovery, and death events are recorded at each time step.
- **Real-Time Visualization:**
  - Network graph updates in real time, with nodes changing color based on infection status.
  - **Four graphs** display:
    - The disease spread network (nodes and edges)
    - New infections per time step (**Red**)
    - New recoveries per time step (**Green**)
    - New deaths per time step (**Blue**)
  - All graphs use **moving averages** for smoother visualization.

## Code Breakdown
### 1. Model Initialization
- The `get_model_params()` function provides user-adjustable settings via Streamlit's sidebar sliders.
- The `DiseaseSpreadModel` class initializes:
  - A scale-free network with `networkx.barabasi_albert_graph`.
  - Each node with a unique size and status (`susceptible` or initially `infected`).

### 2. Disease Spread Mechanism
- **Agent Class:** Each node acts as an agent with rules for:
  - **Interacting with neighbors** (spreading infection with a probability based on size).
  - **Updating status** (transitioning from `susceptible → infected → alive/dead`).
- **Step Function:**
  - At each step, infected nodes try to infect their neighbors.
  - Nodes remain infected for **3 steps**, then either recover (**green**) or die (**blue**) with equal probability.
  - Counts of new infections, recoveries, and deaths are recorded per step.

### 3. Visualization
- The `plot_visuals()` function generates:
  - **A dynamic network visualization** (showing node colors changing over time).
  - **Three smoothed time series graphs** (infection, recovery, death counts per step).
- The visualization updates dynamically using `st.pyplot()` in Streamlit.

## How to Use
1. Clone this repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```
2. Install dependencies:
   ```bash
   pip install streamlit networkx matplotlib numpy
   ```
3. Run the Streamlit application:
   ```bash
   streamlit run script.py
   ```
4. Adjust simulation parameters using the sidebar sliders.
5. Click **"Run Simulation"** to observe the infection spread over time.
6. View the **real-time network visualization and time series plots**.



## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


