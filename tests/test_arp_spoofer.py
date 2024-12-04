import pytest
from unittest.mock import Mock, patch
from src.spoofer.arp_spoofer import ARPSpoofer
from src.core.exceptions import NetworkException

@pytest.fixture
def spoofer():
    with patch('src.spoofer.arp_spoofer.Console'), \
         patch('src.spoofer.arp_spoofer.setup_logger'):
        return ARPSpoofer()

def test_validate_ip_valid(spoofer):
    assert spoofer.validate_ip('192.168.1.1') == True
    assert spoofer.validate_ip('10.0.0.1') == True

def test_validate_ip_invalid(spoofer):
    assert spoofer.validate_ip('256.256.256.256') == False
    assert spoofer.validate_ip('invalid_ip') == False

def test_get_mac_valid_ip(spoofer, mocker):
    mock_srp = mocker.patch('scapy.all.srp')
    mock_srp.return_value = ([Mock(hwsrc='00:11:22:33:44:55')], None)
    
    mac = spoofer.get_mac('192.168.1.1')
    assert mac == '00:11:22:33:44:55'

def test_get_mac_invalid_ip(spoofer):
    with pytest.raises(NetworkException):
        spoofer.get_mac('invalid_ip')

def test_scan_network(spoofer, mocker):
    mock_srp = mocker.patch('scapy.all.srp')
    mock_srp.return_value = (
        [Mock(psrc='192.168.1.1', hwsrc='00:11:22:33:44:55')],
        None
    )
    
    devices = spoofer.scan_network('192.168.1.0/24')
    assert len(devices) == 1
    assert devices[0].ip == '192.168.1.1'
    assert devices[0].mac == '00:11:22:33:44:55'