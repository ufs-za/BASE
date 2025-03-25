# 🧠 Agent-Based Territorial Simulation in Gauteng (South Africa)


## Features

-  **Adjustable number of territories** (e.g., 50 to 1000)
-  **Three distinct agent strategies**:
  - **Agent A (Greedy)**: Moves toward the closest unclaimed territory.
  - **Agent B (Random)**: Moves randomly to unclaimed or available territories.
  - **Agent C (Aggressive)**: Prefers to steal territories from other agents.
-  **Real-time interactive map** (via `pydeck`) with:
  - Custom agent colors (red, blue, green)
  - Territory hover tooltips
  - Dynamic territory expansion
-  **Live-updating bar chart** of territory ownership
-  **Step-by-step or automatic progression** (1 step per second)

---

## 🛠 How to Run the App

### 1. Clone this repository

```bash
git clone https://github.com/your-username/agent-territory-sim.git
cd agent-territory-sim
