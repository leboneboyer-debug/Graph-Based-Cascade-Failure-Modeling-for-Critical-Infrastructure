# simulation/visualze.py

"""Install the required dependencies"""
import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def draw_network_states(graph, title, output_filename=None):
    """Plots the network state color-coding nodes by operational health"""
    plt.figure(figsize=(8, 6))

    color_map = []
    for node in graph.nodes:
        status = graph.nodes[node].get("status", "Operational")
        color_map.append("green" if status == "Operational" else "red")

    pos = nx.spring_layout(graph, seed=50)

    nx.draw(
        graph, pos, with_labels=True, node_color=color_map,
        node_size=200, font_size=10, font_weight="bold",
        arrows=True, edge_color="gray"
    )

    plt.title(title, fontsize=14, fontweight="bold")

    if output_filename:
        plt.savefig(output_filename, format="png", bbox_inches="tight")
        plt.close()
    else:
        plt.show()