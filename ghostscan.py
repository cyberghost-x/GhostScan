#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(description="GhostScan - A Python-based port scanner")
    parser.add_argument("target", help="Target URL or IP address to scan")
    parser.add_argument("-p","--port",help="Port number to scan", default=None,type=int)
    args = parser.parse_args()
    if args.port is not None and args.port not in range(1, 65536):
        print("Error: Port number must be between 1 and 65535.")
        return
    print(f"Target: {args.target}")
    print(f"Port: Default" if args.port is None else f"Port: {args.port}")



if __name__ == "__main__":
    main()