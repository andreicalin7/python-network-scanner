import socket

from colorama import Fore


def discover_host(ip):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(0.5)

    result = sock.connect_ex((ip, 80))

    if result == 0:

        print(Fore.GREEN + f"[LIVE HOST] {ip}")

    sock.close()