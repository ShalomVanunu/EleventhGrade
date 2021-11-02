
from scapy.all import *
from scapy.layers.inet import *

fake_src_IP = "172.20.153.90" #NIR

dest_IP = "172.20.153." #ILAY

for i in range(1,200):
    packet = IP(src= fake_src_IP, dst=dest_IP+str(i))/ICMP()

    send(packet)
