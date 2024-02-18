import socket

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((host, port))
        s.close()
        return True
    except (socket.timeout, socket.error):
        return False

def port_scan(host, ports):
    print("Scanning ports for", host)
    open_ports = []
    for port in ports:
        if scan_port(host, port):
            print("Port", port, "is open.")
            open_ports.append(port)
        else:
            print("Port", port, "is closed.")
    return open_ports

def main():
    host = input("Enter the target host: ")
    specific_scan = input("Do you want to scan specific ports? (yes/no): ").lower()
    
    if specific_scan == "yes":
        ports_input = input("Enter the ports to scan (comma-separated): ")
        ports = [int(p.strip()) for p in ports_input.split(",")]
    else:
        start_port = 1
        end_port = 1024
        ports = list(range(start_port, end_port + 1))

    print("Scanning ports for", host)
    open_ports = port_scan(host, ports)
    print("Open ports on", host + ":", open_ports)

if __name__ == "__main__":
    main()
