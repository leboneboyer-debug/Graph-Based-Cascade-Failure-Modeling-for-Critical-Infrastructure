# main.py

"""Import the required functionality from config.py and engine.py"""
from simulation.engine import intialize_graph, run_sim
from simulation.visualize import draw_network_states

def main():
    print("[*] Initializing Critical Infrastructure Network Graph...")
    grid = intialize_graph()
    
    # Save baseline operational graph
    draw_network_states(grid, "Baseline State: All Systems Operational", "baseline_grid.png")
    print("[+] Baseline visualization saved as 'baseline_grid.png'")
    
    # Execute attack simulation on Substation A
    target = "Substation A"
    print(f"\n[*] Simulating Targeted Kinetic/Cyber Strike on: '{target}'...")
    compromised_grid = run_sim(grid, target)
    
    # Record and show results
    print("\n--- Simulation Vulnerability Report ---")
    for node in compromised_grid.nodes:
        status = compromised_grid.nodes[node]["status"]
        print(f"Node: {node:<25} | Status: {status}")
        
    # Save compromised post-cascade graph
    draw_network_states(compromised_grid, f"Post-Cascade State: Impact of Losing {target}", "compromised_grid.png")
    print("\n[+] Cascade failure visualization saved as 'compromised_grid.png'")

if __name__ == "__main__":
    main()

