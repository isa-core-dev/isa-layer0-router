import json
import time
import sys

def load_matrix_config(config_path="config.json"):
    try:
        with open(config_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def initialize_layer0_matrix():
    config = load_matrix_config()
    if not config:
        sys.exit(1)
        
    router_id = config.get("router_id", "unknown")
    matrix_settings = config.get("layer0_matrix", {})
    nodes = config.get("topology", {}).get("nodes", [])
    
    if not matrix_settings.get("cross_border_routing", False):
        sys.exit(1)
        
    time.sleep(0.5)
    
    for node in nodes:
        time.sleep(0.1)
        
    return True

if __name__ == "__main__":
    success = initialize_layer0_matrix()
    if success:
        sys.exit(0)
    else:
        sys.exit(1)
