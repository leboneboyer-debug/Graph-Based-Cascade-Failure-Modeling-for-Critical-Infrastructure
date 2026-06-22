# simulation/engine.py

""" Required packages for graph-based networks."""
import networkx as nx

"""Import the required nodes and edges from config.py."""
from simulation.config import INFRASTRUCTURE_NODES, DEPENDENCY_EDGES


def intialize_graph():
    """Generates the base network topology."""
    G = nx.DiGraph()

    for node, node_type in INFRASTRUCTURE_NODES.items():
        G.add_node(node, type=node, status="Operational")
    

    G.add_edges_from(DEPENDENCY_EDGES)
    return G

def run_sim(graph, target_node):
    """Simulates node failures and propagates cascading operational losses."""
    # Creates a temporary of out master graph
    sim_graph = graph.copy()


    if target_node not in sim_graph:
        return sim_graph
    
    # Simulate an attack on the network by removing the target node
    sim_graph.remove_node(target_node)

    # Indentify surviving operational status of remaining nodes
    for node in list(sim_graph.nodes):

        # Assets remain operational if they have a path to the power source
        has_grid_power = nx.has_path(sim_graphs, "Offsite Grid", node) if "Offsitr Grid" in sim_graph else False
        has_backup_power = nx.has_path(sim_graph, "Backup Generator Cage", node) if "Backup Generator Cage" in sim_graph else False

        # Ensures that the nodes themselves are not dead
        if node == "Backup Generator Cage" and not has_grid_power:
            sim_graph.nodes[node]["status"] = "Failed"
        elif not (has_grid_power or has_backup_power):
            sim_graph.nodes[node]["status"] = "Failed"

    # Returns the network topology
    return sim_graph 

        




