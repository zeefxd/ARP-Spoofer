from typing import List, Dict

class PacketInfo:
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
    def __init__(self, ip: str, mac: str, hostname: str):
        self.ip = ip
        self.mac = mac
        self.hostname = hostname