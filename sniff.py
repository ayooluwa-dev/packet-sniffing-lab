#!/usr/bin/env python3
"""Small packet sniffer built on Scapy.

Example:
    sudo python3 sniff.py --iface br-da898d0b396c --filter icmp
"""
import argparse
from scapy.all import sniff


def parse_args():
    parser = argparse.ArgumentParser(description="Capture and print network packets.")
    parser.add_argument("--iface", required=True, help="network interface to listen on")
    parser.add_argument("--filter", default="icmp", help="BPF capture filter (default: icmp)")
    parser.add_argument("--count", type=int, default=0, help="stop after this many packets (0 = no limit)")
    parser.add_argument("--full", action="store_true", help="print every field instead of a one-line summary")
    return parser.parse_args()


def main():
    args = parse_args()

    def handle(pkt):
        if args.full:
            pkt.show()
        else:
            print(pkt.summary())

    print(f"Listening on {args.iface} with filter '{args.filter}' (Ctrl+C to stop)")
    sniff(iface=args.iface, filter=args.filter, prn=handle, count=args.count)


if __name__ == "__main__":
    main()
