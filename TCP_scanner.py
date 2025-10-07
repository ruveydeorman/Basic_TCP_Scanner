import scapy.all as scapy
import time
def scanning_ports(TargetIP,PortRange):
	ip_layer = scapy.IP(dst=TargetIP) # "dst" define where sending ip packet
        tcp_layer = scapy.TCP(flags="S",dport=PortRange) # creating tcp packet "dport=target ports" 
	combined_packet = ip_layer / tcp_layer  # this send SYN flag for specific port in target ip with tcp port
	answered, unanswered = scapy.srp(combined_packet,timeout=2, verbose=False) # srp(Send and Receive Packets at Layer 2)
	for sent, receive in answered:
		if received.haslayer(scapy.TCP) and (received.getlayer(scapy.TCP).flags & 2): # checking SYN-ACK flags
			print(f"[+]  {sent.dport} is open")
if __name__=="__main__":
	target = input("Target ip: ")
	start = int(input("Start Port: "))
	end = int(input("End port:"))
	start_time = time.time()
	scanning_ports(target,range(start,end+1))
	end_time = time.time()
	print(f"time of scanning : {end_time-start_time:.2f} second ")