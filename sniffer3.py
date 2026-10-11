#!/usr/bin/env python3
from scapy.all import *

def print_pkt(pkt):
    pkt.show()

pkt = sniff(iface='br-da898d0b396c', filter='net 128.230.0.0/16', prn=print_pkt)
