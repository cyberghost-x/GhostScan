#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(description="GhostScan - A Python-based port scanner")
    parser.add_argument("target", help="Target URL or IP address to scan")
    parser.add_argument("-p","--port",help="Port number to scan", default="Default")
    args = parser.parse_args()
    print(f"Target: {args.target}")
    print(f"Port: {args.port}")



if __name__ == "__main__":
    main()