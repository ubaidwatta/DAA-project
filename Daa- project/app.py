import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Function to visualize the graph
def visualize_graph(G, shortest_path=None):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(8, 6))
    
    nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=700, edgecolors='black')
    nx.draw_networkx_edges(G, pos, width=2, edge_color='gray')
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    
    if shortest_path:
        path_edges = list(zip(shortest_path, shortest_path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
        nx.draw_networkx_nodes(G, pos, nodelist=shortest_path, node_color='orange')
    
    plt.title("Dijkstra's Shortest Path Visualization", fontsize=14)
    plt.axis('off')
    st.pyplot(plt)

# Streamlit app
def main():
    st.title("🧭 Dijkstra's Shortest Path Visualizer")
    st.markdown("Enter your graph edges below (like `A B 4` means A–B with weight 4).")

    # Get edge input from user
    edge_input = st.text_area("Enter edges (one per line):", height=150, placeholder="A B 4\nA C 7\nB D 3\nD E 2\nE Z 5")

    if edge_input.strip():
        G = nx.Graph()
        edges = []

        for line in edge_input.strip().splitlines():
            try:
                u, v, w = line.strip().split()
                w = float(w)
                G.add_edge(u.upper(), v.upper(), weight=w)
                edges.append((u.upper(), v.upper(), w))
            except ValueError:
                st.warning(f"Invalid format in line: `{line}`. Expected format: `Node1 Node2 Weight`")

        if edges:
            st.success("✅ Graph created successfully!")

            # Select source and target nodes
            nodes = sorted(G.nodes())
            col1, col2 = st.columns(2)
            with col1:
                source = st.selectbox("Select Source Node:", nodes)
            with col2:
                target = st.selectbox("Select Target Node:", nodes)

            if st.button("Find Shortest Path"):
                if nx.has_path(G, source, target):
                    path = nx.dijkstra_path(G, source, target)
                    distance = nx.dijkstra_path_length(G, source, target)
                    st.success(f"Shortest path: {' → '.join(path)}")
                    st.info(f"Total distance: {distance}")
                    visualize_graph(G, path)
                else:
                    st.error(f"No path exists between {source} and {target}!")

    else:
        st.info("Enter graph data above to begin.")

if __name__ == "__main__":
    main()

