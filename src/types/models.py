from typing import List, Dict

"""Data models for the ARP spoofer application."""

class PacketInfo:
    """
    Represents captured packet information.

    Attributes:
        time (str): Timestamp of packet capture
        src (str): Source IP address
        dst (str): Destination IP address
        payload (str): Packet payload data
    """
    def __init__(self, time: str, src: str, dst: str, payload: str):
        self.time = time
        self.src = src
        self.dst = dst
        self.payload = payload

    def to_dict(self):
        return {
            'time': self.time,
            'src': self.src,
            'dst': self.dst,
            'payload': self.payload,
        }

class Device:
    """
    Represents a network device.

    Attributes:
        ip (str): Device IP address
        mac (str): Device MAC address
        hostname (str): Device hostname
    """
    def __init__(self, ip: str, mac: str, hostname: str):
        self.ip = ip
        self.mac = mac
        self.hostname = hostname