import subprocess
import pandas as pd
from datetime import datetime

# Define your network range
network_range = "192.168.1.0/24"

# Run nmap command
def run_nmap_scan():
    result = subprocess.check_output(['nmap', '-sP', network_range]).decode()
    return result

# Parse nmap results
def parse_nmap_results(results):
    devices = []
    lines = results.split("\n")
    for i, line in enumerate(lines):
        if "Nmap scan report for" in line:
            ip_address = line.split()[-1]
            hostname = line.split()[-2] if "(" in line else "Unknown"
            devices.append({
                "IP Address": ip_address,
                "Hostname": hostname,
                "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
    return devices

# Save results to Excel
def save_to_excel(devices, file_name="network_inventory.xlsx"):
    df = pd.DataFrame(devices)
    df.to_excel(file_name, index=False)
    print(f"Results saved to {file_name}")

if __name__ == "__main__":
    print("Running nmap scan...")
    nmap_results = run_nmap_scan()
    devices = parse_nmap_results(nmap_results)
    save_to_excel(devices)
