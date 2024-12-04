class SpooferException(Exception):
    """Base exception for the spoofer module."""
    pass

class NetworkException(SpooferException):
    """Exception raised for network-related errors."""
    pass