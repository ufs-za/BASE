import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import random
import time

# Streamlit UI setup
st.title("Misinformation Dynamic Network Simulation")
st.sidebar.header("Simulation Parameters")

# Customizable parameters
N = st.sidebar.slider("Number of Agents", min_value=50, max_value=500, value=100, step=10)
misinformation_spread_prob = st.sidebar.slider("Misinformation Spread Probability", min_value=0.0, max_value=1.0, value=0.3, step=0.05)
fact_check_prob = st.sidebar.slider("Fact-Checking Probability", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
epsilon = st.sidebar.slider("Epsilon (E-Greedy Believers)", min_value=0.0, max_value=1.0, value=0.1, step=0.05)
steps = st.sidebar.slider("Simulation Steps", min_value=50, max_value=500, value=200, step=10)

# Create a Scale-Free Network
G = nx.barabasi_albert_graph(N, 3)
network_pos = nx.spring_layout(G)  # Fixed layout for consistent visualization

# Assign belief states to nodes
belief_states = ["Believer", "Skeptic", "Neutral", "Influencer"]
node_colors = {}
node_sizes = {}
skep_strategies = {}  # Store UCB skeptics
agent_types = {"Believer": set(), "Skeptic": set(), "Neutral": set(), "Influencer": set()}
rewards = {"Skeptic": [0], "Believer": [0]}  # Track cumulative rewards over time

for node in G.nodes():
    belief = random.choices(belief_states, weights=[0.4, 0.3, 0.2, 0.1])[0]
    if belief == "Skeptic":
        skep_strategies[node] = "UCB"  # All skeptics use UCB
    elif belief == "Believer":
        skep_strategies[node] = "E-Greedy"  # All believers use E-Greedy
    agent_types[belief].add(node)
    node_colors[node] = {"Believer": "red", "Skeptic": "blue", "Neutral": "gray", "Influencer": "green"}[belief]
    node_sizes[node] = {"Believer": 100, "Skeptic": 100, "Neutral": 80, "Influencer": 300}[belief]

# Initialize tracking metrics
belief_counts = {"Believers": [len(agent_types["Believer"])],
                 "Skeptics": [len(agent_types["Skeptic"])],
                 "Neutrals": [len(agent_types["Neutral"])],
                 "Influencers": [len(agent_types["Influencer"])],
                 "Rewards_Skeptic": [0],
                 "Rewards_Believer": [0]}

# Streamlit visualization setup
st.sidebar.write("Click the button below to start the simulation.")
if st.sidebar.button("Start Simulation"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    network_plot = st.empty()
    graph_plot = st.empty()
    
    for t in range(steps):
        reward_skeptic = rewards["Skeptic"][-1]
        reward_believer = rewards["Believer"][-1]
        
        for node in list(G.nodes()):
            neighbors = list(G.neighbors(node))
            if not neighbors:
                continue
            target = random.choice(neighbors)
            
            if node in agent_types["Believer"]:  # E-Greedy believers spreading misinformation
                if random.random() < epsilon:
                    target = random.choice(neighbors)  # Explore new target
                if random.random() < misinformation_spread_prob and target in agent_types["Neutral"]:
                    agent_types["Believer"].add(target)
                    agent_types["Neutral"].remove(target)
                    node_colors[target] = "red"
                    reward_believer += 1
                elif target in agent_types["Influencer"]:
                    agent_types["Believer"].add(target)
                    node_colors[target] = "red"
                    reward_believer += 2
            
            elif node in agent_types["Skeptic"]:  # UCB skeptics counter misinformation
                if node in skep_strategies and skep_strategies[node] == "UCB":
                    if random.random() < fact_check_prob and target in agent_types["Believer"]:
                        agent_types["Skeptic"].add(target)
                        agent_types["Believer"].remove(target)
                        node_colors[target] = "blue"
                        reward_skeptic += 1
                    elif target in agent_types["Influencer"] and node_colors[target] == "red":
                        agent_types["Skeptic"].add(target)
                        node_colors[target] = "blue"
                        reward_skeptic += 2
        
        rewards["Believer"].append(reward_believer)
        rewards["Skeptic"].append(reward_skeptic)
        
        belief_counts["Believers"].append(len(agent_types["Believer"]))
        belief_counts["Skeptics"].append(len(agent_types["Skeptic"]))
        belief_counts["Neutrals"].append(len(agent_types["Neutral"]))
        belief_counts["Influencers"].append(len(agent_types["Influencer"]))
        
        progress_bar.progress((t + 1) / steps)
        status_text.text(f"Simulation Step {t + 1}/{steps}")
        
        if t % 10 == 0:
            fig, ax = plt.subplots(figsize=(12, 10))
            nx.draw(G, pos=network_pos, node_color=[node_colors[n] for n in G.nodes()], node_size=[node_sizes[n] for n in G.nodes()], edge_color="lightgray", with_labels=False)
            network_plot.pyplot(fig)
            
            fig, axs = plt.subplots(1, 2, figsize=(18, 6))
            axs[0].plot(range(len(belief_counts["Believers"])), belief_counts["Believers"], label="Believers (E-Greedy)", color="red")
            axs[0].plot(range(len(belief_counts["Skeptics"])), belief_counts["Skeptics"], label="Skeptics (UCB)", color="blue")
            axs[0].set_title("Believers vs. Skeptics Over Time")
            axs[0].legend()
            
            axs[1].plot(range(len(belief_counts["Neutrals"])), belief_counts["Neutrals"], label="Neutrals", color="gray")
            axs[1].set_title("Neutral Count Over Time")
            axs[1].legend()
            
            graph_plot.pyplot(fig)
    
    st.success("Simulation Complete")
