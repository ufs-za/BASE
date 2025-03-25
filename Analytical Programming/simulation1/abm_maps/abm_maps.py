import streamlit as st
import pandas as pd
import numpy as np
import random
import pydeck as pdk
import time
from geopy.distance import geodesic

st.set_page_config(page_title="Gauteng Territory Simulation", layout="wide")
st.title("🏙️ Agent-Based Simulation: Gauteng Province")

# --- Constants ---
AGENT_COLORS = {'Agent A': [255, 0, 0], 'Agent B': [0, 0, 255], 'Agent C': [0, 255, 0]}  # RGB
AGENT_NAMES = list(AGENT_COLORS.keys())
GAUTENG_BOUNDS = {
    'lat_min': -26.7,
    'lat_max': -25.5,
    'lon_min': 27.5,
    'lon_max': 28.7
}

# --- Sidebar Controls ---
st.sidebar.markdown("### Simulation Controls")

# Choose number of territories (adjustable)
num_territories = st.sidebar.slider("Number of Territories", 50, 1000, 500, step=50)

# --- Generate Random Territory Points in Gauteng ---
def generate_gauteng_territories(n):
    lats = np.random.uniform(low=GAUTENG_BOUNDS['lat_min'], high=GAUTENG_BOUNDS['lat_max'], size=n)
    lons = np.random.uniform(low=GAUTENG_BOUNDS['lon_min'], high=GAUTENG_BOUNDS['lon_max'], size=n)
    names = [f"G{i+1}" for i in range(n)]
    return pd.DataFrame({'name': names, 'lat': lats, 'lon': lons, 'owner': [None]*n})

# --- Session State Initialization ---
if 'simulation_started' not in st.session_state:
    st.session_state.simulation_started = False
if 'territories' not in st.session_state:
    st.session_state.territories = None
if 'agents' not in st.session_state:
    st.session_state.agents = None
if 'step' not in st.session_state:
    st.session_state.step = 0
if 'auto_running' not in st.session_state:
    st.session_state.auto_running = False
if 'remaining_steps' not in st.session_state:
    st.session_state.remaining_steps = 0
if 'num_territories' not in st.session_state:
    st.session_state.num_territories = num_territories

# --- Core Functions ---
def get_adjacent(current_idx, total):
    return [i for i in range(total) if i != current_idx]

def reset_simulation():
    n = st.session_state.num_territories
    territories = generate_gauteng_territories(n)
    start_idxs = random.sample(range(n), 3)
    agents = {
        AGENT_NAMES[i]: {
            'color': AGENT_COLORS[AGENT_NAMES[i]],
            'location': start_idxs[i],
            'owned': set(),
            'cooldown': 0
        }
        for i in range(3)
    }
    st.session_state.territories = territories
    st.session_state.agents = agents
    st.session_state.step = 0
    st.session_state.simulation_started = True
    st.session_state.auto_running = False
    st.session_state.remaining_steps = 0

if st.sidebar.button("🚀 Start Simulation"):
    st.session_state.num_territories = num_territories
    reset_simulation()
# --- Define run_step before any button that might use it ---
def run_step():
    move_attempts = {}
    territories = st.session_state.territories
    agents = st.session_state.agents
    num_territories = st.session_state.num_territories

    for agent_name, agent in agents.items():
        if agent['cooldown'] > 0:
            agent['cooldown'] -= 1
            continue

        current_idx = agent['location']
        current_pos = (territories.at[current_idx, 'lat'], territories.at[current_idx, 'lon'])
        options = get_adjacent(current_idx, num_territories)

        if agent_name == "Agent A":  # Greedy
            unclaimed = [
                (i, geodesic(current_pos, (territories.at[i, 'lat'], territories.at[i, 'lon'])).km)
                for i in options if territories.at[i, 'owner'] is None
            ]
            target_idx = min(unclaimed, key=lambda x: x[1])[0] if unclaimed else random.choice(options)

        elif agent_name == "Agent B":  # Random
            unclaimed = [i for i in options if territories.at[i, 'owner'] is None]
            target_idx = random.choice(unclaimed) if unclaimed else random.choice(options)

        elif agent_name == "Agent C":  # Aggressive
            claimed_by_others = [
                i for i in options
                if territories.at[i, 'owner'] is not None and territories.at[i, 'owner'] != agent_name
            ]
            if claimed_by_others:
                target_idx = random.choice(claimed_by_others)
            else:
                unclaimed = [i for i in options if territories.at[i, 'owner'] is None]
                target_idx = random.choice(unclaimed) if unclaimed else random.choice(options)

        if target_idx not in move_attempts:
            move_attempts[target_idx] = []
        move_attempts[target_idx].append(agent_name)

    for target_idx, contenders in move_attempts.items():
        winner = random.choice(contenders) if len(contenders) > 1 else contenders[0]
        previous_owner = territories.at[target_idx, 'owner']
        territories.at[target_idx, 'owner'] = winner
        agents[winner]['location'] = target_idx
        agents[winner]['owned'].add(target_idx)

        if previous_owner and previous_owner != winner:
            agents[winner]['cooldown'] = 1

    st.session_state.step += 1

if st.session_state.simulation_started:
    auto_steps = st.sidebar.slider("Auto Steps (seconds)", 1, 100, 10)

    if st.sidebar.button("▶️ Run Automatically"):
        st.session_state.auto_running = True
        st.session_state.remaining_steps = auto_steps
        st.rerun()

    if st.sidebar.button("⏭️ Next Step"):
        run_step()

    st.sidebar.write(f"Current Step: **{st.session_state.step}**")


def render_map():
    territories = st.session_state.territories
    agents = st.session_state.agents

    layer_data = []
    for idx, row in territories.iterrows():
        owner = row['owner']
        color = agents[owner]['color'] if owner else [180, 180, 180]
        layer_data.append({
            'lat': row['lat'],
            'lon': row['lon'],
            'color': color,
            'name': row['name'],
            'owner': owner or "Unclaimed"
        })

    df_map = pd.DataFrame(layer_data)

    layer = pdk.Layer(
        "ScatterplotLayer",
        data=df_map,
        get_position='[lon, lat]',
        get_color='color',
        get_radius=300,
        pickable=True
    )

    view_state = pdk.ViewState(
        latitude=-26.2,
        longitude=28.2,
        zoom=8.5,
        pitch=0
    )

    st.pydeck_chart(pdk.Deck(
        layers=[layer],
        initial_view_state=view_state,
        tooltip={"text": "{name}\nOwner: {owner}"},
        map_style=None
    ))

# --- Auto-Run Engine ---
if st.session_state.simulation_started:
    if st.session_state.auto_running and st.session_state.remaining_steps > 0:
        run_step()
        st.session_state.remaining_steps -= 1
        time.sleep(1)
        st.rerun()
    elif st.session_state.remaining_steps == 0:
        st.session_state.auto_running = False

# --- Main Map & Bar Chart ---
if st.session_state.simulation_started:
    render_map()

    st.subheader("📊 Territories Owned Over Time")
    stats = {
        agent: len(data['owned'])
        for agent, data in st.session_state.agents.items()
    }

    df_stats = pd.DataFrame.from_dict(stats, orient='index', columns=['Territories']).rename_axis("Agent")

    import matplotlib.pyplot as plt

    # Show table
    st.dataframe(df_stats)

    # Custom-colored bar chart using matplotlib
    st.subheader("📊 Bar Chart (Color-coded)")

    fig, ax = plt.subplots()
    bars = ax.bar(
        df_stats.index,
        df_stats['Territories'],
        color=[
            '#FF0000',  # Red for Agent A
            '#0000FF',  # Blue for Agent B
            '#00FF00'   # Green for Agent C
        ]
    )

    ax.set_ylabel("Territories")
#    ax.set_ylim(0, st.session_state.num_territories)
    ax.set_ylim(0, 200)
    ax.set_title("Territories Owned by Agent")
    st.pyplot(fig)

else:
    st.info("Click **Start Simulation** to begin.")
