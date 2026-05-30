#!/usr/bin/env python3

#-------Check installation-----------#

def check_pandas():
    try:
        import pandas as pd
        print(f"[OK] pandas ({pd.__version__}) - Data manipulation ready")
    except ImportError:
        print("[!] pandas is NOT installed")
        
def check_numpy():
    try:
        import numpy as np
        print(f"[OK] numpy ({np.__version__}) - Numerical computation ready")
    except ImportError:
        print("[!] numpy is NOT installed")
        
def check_requests():
    try:
        import requests as rq
        print(f"[OK] requests ({rq.__version__}) - Network access ready")
    except ImportError:
        print("[!] request is NOT installed")
        
def check_matplotlib():
    try:
        import matplotlib as plt
        print(f"[OK] matplotlib ({plt.__version__}) - Visualization ready")
    except ImportError:
        print("[!] matplotlib is NOT installed")
            
if __name__ == "__main__":
    check_numpy()
    check_pandas()
    check_requests()
    check_matplotlib()