import socket
import threading


def scan_ports(host, start_port, end_port):
    
    open_ports = []
    open_ports_lock = threading.Lock()

    def _scan_port(host, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((host, port))
            if result == 0:
                with open_ports_lock:
                    open_ports.append(port)
            s.close()
        except:
            pass

    for port in range(start_port, end_port+1):
        thread = threading.Thread(target=_scan_port, args=(host, port))
        thread.start()

    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

    # saving results in a file
    with open("open_ports.txt", "w") as f:
        if open_ports:
            result_str = "{" + ", ".join(map(str, open_ports)) + "}"
            f.write(f"Open ports: {result_str}")
        else:
            f.write("No open ports found.")

    return open_ports


scan_ports("localhost", 1, 1024)