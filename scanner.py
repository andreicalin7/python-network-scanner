import socket

from colorama import Fore

from logger import log_result

import threading

print_lock = threading.Lock()

def scan_port(target, port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:

        message = f"[OPEN] Port {port}"

        with print_lock:
            print(Fore.GREEN + message)

        log_result(message)

        # Banner grabbing
        try:

            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")

            banner = sock.recv(1024).decode().strip()

            if banner:
                banner_message = f"[BANNER] Port {port}: {banner}"

                with print_lock:
                    print(Fore.CYAN + banner_message)

                log_result(banner_message)

        except:
            pass

    else:
        pass

    sock.close()