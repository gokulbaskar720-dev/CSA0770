# devops_health_check.py

import subprocess

services = ["docker", "nginx", "jenkins"]

for service in services:
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )
        status = result.stdout.strip()
        if status == "active":
            print(f"{service}: Running")
        else:
            print(f"{service}: Not Running")
    except Exception as e:
        print(f"Error checking {service}: {e}")
