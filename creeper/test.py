from scapy.all import *
from scapy.contrib.igmpv3 import IGMPv3,IGMPv3mq,IGMP,IGMPv3gr
from scapy.contrib.igmpv3 import IGMPv3mr

p_join = Ether(dst='01:00:5e:00:00:16', src='00:0c:29:c8:31:8a') / IP(src='192.168.204.139', dst='224.0.0.22', tos=0xc0) /IGMPv3() /IGMPv3mr(numgrp=1) /IGMPv3gr(rtype=4, maddr="239.1.1.1")
p_join.show()
sendp(p_join,iface='en1')
