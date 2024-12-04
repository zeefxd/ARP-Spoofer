# API Reference

## ARPSpoofer Class

```python
class ARPSpoofer:
    def __init__(self, target_ip: str = None, gateway_ip: str = None, patterns: list = None)
```
Main class for ARP spoofing operations.

## Methods
### scan_network
```python
def scan_network(self, ip_range: str) -> list
```
Scans network for active devices.

### spoof
```python
def spoof(self, target_ip: str, spoof_ip: str)
```
Sends ARP spoofing packets.

### restore
```python
def restore(self, destination_ip: str, source_ip: str)
```
Restores ARP tables.

### get_mac
```python
def get_mac(self, ip: str) -> str
```
Gets the MAC address for a given IP.

### run
```python
def run(self, format: str = None)
```
Main execution method.


