import socket
from datetime import datetime

open_ports = []

def scan_port(target, port, file):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            message = f"[OPEN] Port {port} ({service})"
            print(message)
            file.write(message + "\n")
            open_ports.append(port)

        s.close()
    except:
        pass

def get_port(prompt):
    while True:
        try:
            port = int(input(prompt))
            if 1 <= port <= 65535:
                return port
            else:
                print("❌ Port must be between 1 and 65535")
        except ValueError:
            print("❌ Please enter only a NUMBER")

def main():
    target = input("Enter target IP: ")
    start_port = get_port("Enter start port: ")
    end_port = get_port("Enter end port: ")

    if start_port > end_port:
        print("❌ Start port must be less than end port")
        return

    start_time = datetime.now()

    with open("scan_results.txt", "w") as file:
        header = f"Mini Nmap Scan Report\nTarget: {target}\nStart Time: {start_time}\n"
        header += "-" * 50 + "\n"
        print(header)
        file.write(header)

        for port in range(start_port, end_port + 1):
            scan_port(target, port, file)

        end_time = datetime.now()
        duration = end_time - start_time

        summary = "\n" + "-" * 50 + "\n"
        summary += f"Scan Completed\nEnd Time: {end_time}\n"
        summary += f"Scan Duration: {duration}\n"
        summary += f"Total Open Ports Found: {len(open_ports)}\n"

        print(summary)
        file.write(summary)

    print("📁 Results saved to scan_results.txt")

if __name__ == "__main__":
    main()

