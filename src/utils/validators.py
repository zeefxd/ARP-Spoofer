import re

def validate_ip(ip: str) -> bool:
    """Validate IP address format and octet ranges."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if not pattern.match(ip):
        return False
    parts = ip.split(".")
    for part in parts:
        if not 0 <= int(part) <= 255:
            return False
    return True