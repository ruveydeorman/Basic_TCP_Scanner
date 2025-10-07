# 🔍 TCP SYN Port Scanner

This project is a simple TCP SYN port scanner written in Python using the Scapy library.  
It sends SYN packets to a target IP address across a specified port range and identifies which ports are open based on SYN-ACK responses.

## Features
- TCP scanning
- Custom IP and port range input
- Displays open ports in terminal
- Measures total scan duration

## Installation
```bash
sudo apt update sudo apt install python3-pip pip install scapy

```

## Usage
```bash
sudo python3 tcp_scanner.py
```


**Example Input:**
```bash
Target ip: 10.0.2.5
Start Port: 60
End Port: 100
```


**Example Output:**
```bash
[+] 80 is open
timeof scanning: 2.77 second
```


## Disclaimer

This tool is intended for educational and authorized testing purposes only.  
Unauthorized scanning may violate laws and network policies.

## Author

Rüveyde Orman  
📎 [LinkedIn](https://linkedin.com/in/ruveydeorman)
