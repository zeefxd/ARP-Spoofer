import argparse
import sys
from rich.console import Console
from src.spoofer.arp_spoofer import ARPSpoofer
from src.utils.validators import validate_ip
from src.utils.logger import setup_logger

"""
Main entry point for the ARP spoofer application.

Usage:
    python -m src.main [-t TARGET_IP] [-g GATEWAY_IP] [-p PATTERNS] [-f FORMAT]
"""

def main():
    console = Console()
    logger = setup_logger("arp_spoofer_main", console)

    ascii_art = r"""
    ▄▄▄      ██▀███  ██▓███       ██████ ██▓███  ▒█████  ▒█████   ███████▓███▄    █  ▄████ 
    ▒████▄   ▓██ ▒ ██▓██░  ██▒   ▒██    ▒▓██░  ██▒██▒  ██▒██▒  ██▓██   ▓██▒██ ▀█   █ ██▒ ▀█▒
    ▒██  ▀█▄ ▓██ ░▄█ ▓██░ ██▓▒   ░ ▓██▄  ▓██░ ██▓▒██░  ██▒██░  ██▒████ ▒██▓██  ▀█ ██▒██░▄▄▄░
    ░██▄▄▄▄██▒██▀▀█▄ ▒██▄█▓▒ ▒     ▒   ██▒██▄█▓▒ ▒██   ██▒██   ██░▓█▒  ░██▓██▒  ▐▌██░▓█  ██▓
    ▓█   ▓██░██▓ ▒██▒██▒ ░  ░   ▒██████▒▒██▒ ░  ░ ████▓▒░ ████▓▒░▒█░  ░██▒██░   ▓██░▒▓███▀▒
    ▒▒   ▓▒█░ ▒▓ ░▒▓▒▓▒░ ░  ░   ▒ ▒▓▒ ▒ ▒▓▒░ ░  ░ ▒░▒░▒░░ ▒░▒░▒░ ▒ ░  ░▓ ░ ▒░   ▒ ▒ ░▒   ▒ 
    ▒   ▒▒ ░ ░▒ ░ ▒░▒ ░        ░ ░▒  ░ ░▒ ░      ░ ▒ ▒░  ░ ▒ ▒░ ░     ▒ ░ ░░   ░ ▒░ ░   ░ 
    ░   ▒    ░░   ░░░          ░  ░  ░ ░░      ░ ░ ░ ▒ ░ ░ ░ ▒  ░ ░   ▒ ░  ░   ░ ░░ ░   ░ 
        ░  ░  ░                      ░             ░ ░     ░ ░        ░          ░      ░ 
                                                                                            
                                        ARP SPOOFING TOOL
                                         Author: @zeefxd
    """
    console.print(ascii_art, style="red bold")

    parser = argparse.ArgumentParser(description="ARP Spoofer with pattern matching")
    parser.add_argument("-t", "--target", help="Target IP address")
    parser.add_argument("-g", "--gateway", help="Gateway IP address")
    parser.add_argument("-p", "--patterns", nargs="+", help="Patterns to match in payload")
    parser.add_argument("-f", "--format", choices=["txt", "json", "html", "csv"], default=None, help="Output format for captured data")
    args = parser.parse_args()

    if args.target and not validate_ip(args.target):
        logger.error("Invalid target IP address.")
        sys.exit(1)
    if args.gateway and not validate_ip(args.gateway):
        logger.error("Invalid gateway IP address.")
        sys.exit(1)

    spoofer = ARPSpoofer(target_ip=args.target, gateway_ip=args.gateway, patterns=args.patterns)
    spoofer.run(format=args.format)

if __name__ == "__main__":
    main()