from colorama import init

from config import TARGET, START_PORT, END_PORT
from scanner import scan_port
from concurrent.futures import ThreadPoolExecutor
from discover import discover_host

init(autoreset=True)

print(f"Scanning target: {TARGET}")
print(f"Port range: {START_PORT}-{END_PORT}\n")


with ThreadPoolExecutor(max_workers=100) as executor:

    for port in range(START_PORT, END_PORT + 1):
        executor.submit(scan_port, TARGET, port)

print("\nHost Discovery:\n")

base_ip = "192.168.1."

with ThreadPoolExecutor(max_workers=100) as executor:

    for i in range(1, 255):

        ip = base_ip + str(i)

        executor.submit(discover_host, ip)