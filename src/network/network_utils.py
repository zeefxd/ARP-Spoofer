import socket
from rich.table import Table
from rich.console import Console
from src.models.models import Device

"""Network utility functions for device discovery and hostname resolution."""

def get_hostname(ip: str) -> str:
    """
    Resolve hostname for IP address.

    Args:
        ip (str): IP address to resolve

    Returns:
        str: Hostname or 'unknown' if resolution fails
    """
    try:
        return socket.gethostbyaddr(ip)[0]
    except socket.herror:
        return "unknown"

def display_devices(console: Console, devices: list):
    """
    Display discovered devices in a formatted table.

    Args:
        console (Console): Rich console instance
        devices (list): List of Device objects
    """
    table = Table(title="Network Devices")
    table.add_column("IP Address", style="cyan")
    table.add_column("MAC Address", style="magenta")
    table.add_column("Hostname", style="green")

    for device in devices:
        table.add_row(device.ip, device.mac, device.hostname)

    console.print(table)