from scapy.all import *
from scapy.layers.inet import *


fake_src_IP = "172.20.153.90" #NIR
dest_IP = "172.20.153.127" #ILAY

packet = IP(src= fake_src_IP,dst=dest_IP)/TCP(dport=80,flags="S")
send(packet)