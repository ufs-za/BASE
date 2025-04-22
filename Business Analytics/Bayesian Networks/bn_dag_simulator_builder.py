import streamlit as st
from pgmpy.models import DiscreteBayesianNetwork
import networkx as nx
import matplotlib.pyplot as plt
import ast

# Configure Streamlit page
st.set_page_config(page_title="Bayesian Network Builder", layout="centered")

# App title and instructions
st.title("Bayesian Network Builder")
st.markdown(
    """
Build and visualise your own Bayesian Network using `pgmpy`.

### ✍️ Instructions:
- Enter your edges below in Python list format.
- Each tuple represents a directed edge from one node to another.

Example:
```python
[('A', 'B'), ('B', 'C')]
```"""
)

# Text area for user input
user_input = st.text_area("Type your edge list here:")

# The button that triggers network processing
if st.button("Process Network"):
    if not user_input:
        st.warning("Please enter a list of 2‑element tuples before processing.")
    else:
        try:
            parsed = ast.literal_eval(user_input)

            # Validate format
            if isinstance(parsed, list) and all(isinstance(e, tuple) and len(e) == 2 for e in parsed):
                st.success("✅ Edges parsed successfully!")

                # Optional: build the pgmpy model to check structure
                model = DiscreteBayesianNetwork(parsed)

                # Build a NetworkX DiGraph for visualization
                G = nx.DiGraph()
                G.add_edges_from(parsed)

                # Compute layout
                pos = nx.spring_layout(G)

                # Create Matplotlib figure with automatic padding
                fig, ax = plt.subplots(figsize=(6, 6), constrained_layout=True)

                # Draw nodes and labels
                nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=2000, ax=ax)
                nx.draw_networkx_labels(G, pos, font_size=14, font_weight="bold", ax=ax)

                # Draw arrows manually
                for src, dst in G.edges():
                    ax.annotate(
                        "",
                        xy=pos[dst],
                        xytext=pos[src],
                        arrowprops=dict(
                            arrowstyle="->",
                            lw=2,
                            shrinkA=15,
                            shrinkB=15
                        )
                    )

                # Add margin so nothing is cut off
                ax.margins(0.2)
                ax.set_axis_off()

                # Centre the plot in the page
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    st.pyplot(fig, use_container_width=True)

            else:
                st.error("Input must be a Python list of 2‑element tuples, e.g. [('A','B'),('B','C')].")

        except Exception as e:
            st.error(f"Could not parse your input. Please check the format.\n\n**Error:** {e}")
