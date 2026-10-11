#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    print(pkt.summary())

pkt = sniff(iface='br-da898d0b396c', filter='icmp', prn=print_pkt)
