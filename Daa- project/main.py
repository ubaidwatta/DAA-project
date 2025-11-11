import networkx as nx
import matplotlib.pyplot as plt

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
    plt.show()

def main():
    G = nx.Graph()
    G.add_weighted_edges_from([
        ('A', 'B', 4),
        ('A', 'C', 7),
        ('B', 'C', 1),
        ('B', 'D', 4),
        ('C', 'D', 8),
        ('C', 'E', 7),
        ('D', 'E', 2),
        ('D', 'Z', 2),
        ('E', 'Z', 3)
    ])

    # Display available nodes
    nodes = sorted(list(G.nodes()))
    print("Available nodes in the graph:")
    print(", ".join(nodes))
    print()

    # Get source node from user
    while True:
        source = input("Enter the source node: ").strip().upper()
        if source in G.nodes():
            break
        else:
            print(f"Invalid node '{source}'. Please choose from: {', '.join(nodes)}")
    
    # Get target node from user
    while True:
        target = input("Enter the target node: ").strip().upper()
        if target in G.nodes():
            break
        else:
            print(f"Invalid node '{target}'. Please choose from: {', '.join(nodes)}")

    # Check if path exists
    if not nx.has_path(G, source, target):
        print(f"\nNo path exists between {source} and {target}!")
        return

    # Calculate shortest path
    shortest_path = nx.dijkstra_path(G, source, target)
    shortest_distance = nx.dijkstra_path_length(G, source, target)

    print(f"\nShortest path from {source} to {target}: {' -> '.join(shortest_path)}")
    print(f"Total distance: {shortest_distance}")

    visualize_graph(G, shortest_path)

if __name__ == "__main__":
    main()