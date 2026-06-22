# simulation/config.py

# Infrastructure Nodes defined by their functional types
INFRASTRUCTURE_NODES = {
    "Offside Grid:": "External Source",
    "Substation A": "Distribution",
    "Substation B": "Distrubution",
    "Backup Generator Cage": "Resilience",
    "Mission Control Center": "Critical Asset",
    "Communications Tower": "Critical Assest"
}

DEPENDENCY_EDGES = {
    ("Offsite Grid", "Substation A"),
    ("Offsite Grid", "Substation B"),
    ("Substation A", "Backup Generator Cage"),
    ("Substation B", "Mission Control Center"),
    ("Backup Generator Cage", "Mission Control Center"),
    ("Backup Generator Cage", "Communications Tower")
}