# Mini Nmap - Linux Network Scanner (Python)

Mini Nmap is a lightweight network scanning tool developed using Python on Linux. 
This project is a simplified version of Nmap, designed for learning and demonstrating 
core networking concepts such as port scanning, service detection, and socket programming.

## Features
- Target host scanning
- Custom port range scanning
- Open port detection
- Service name identification
- Scan time calculation
- Scan result logging to file
- Input validation and error handling

## Technologies Used
- Python 3
- Linux (Ubuntu)
- Socket Programming
- TCP/IP Networking

## How It Works
The tool uses TCP socket connections to check if a port is open on the target system. 
If a connection is successful, the port is marked as open and the associated service name is displayed.

## How to Run

1. Clone the repository
git clone https://github.com/Madhesh0203/Mini-nmap
cd mini-nmap


2. Run the scanner
python3 mini_nmap.py


3. Enter:
- Target IP Address
- Start Port
- End Port

## Output
- Open ports are displayed in the terminal
- Full scan report is saved to `scan_results.txt`

## Sample Use Case
- Scanning your local machine (127.0.0.1)
- Scanning a lab virtual machine
- Learning how network scanners work

## Ethical Notice
This tool is created for educational purposes only. 
Scan only systems you own or have explicit permission to test.

## Author
Madheshwaran  
BE CSE | Linux & Networking | Python
