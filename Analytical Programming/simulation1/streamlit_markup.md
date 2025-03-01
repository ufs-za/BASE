st.markdown(
    """
    **Scale-Free Network Disease Spread Simulation**

    This simulation models disease spread in a **scale-free network** using an agent-based approach. 
    Nodes represent individuals, where **red indicates infection, green represents recovery, and blue signifies death**. 
    The spread follows **proximity-based transmission**, with larger nodes taking longer to infect smaller ones. 
    After 3 time steps, an infected node **recovers (turns green) or dies (turns blue) with a 50% probability**. 
    Users can adjust the number of agents, infection probability, and experiment duration.

    **Visualizations:**
    - A **real-time network graph** showing nodes changing color as infection progresses.
    - **Three smoothed time series plots**:
      - Infection spread over time (**Red**).
      - Number of recoveries per step (**Green**).
      - Number of deaths per step (**Blue**).

    Adjust parameters and run the simulation to observe how disease spreads in a complex network.
    """
)
