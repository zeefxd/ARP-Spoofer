import pytest
from unittest.mock import patch, MagicMock
from src.spoofer.arp_spoofer import ARPSpoofer
from src.core.exceptions import NetworkException

@pytest.fixture
def spoofer():
    return ARPSpoofer(target_ip="192.168.1.10", gateway_ip="192.168.1.1")

def test_get_mac_valid_ip(spoofer):
    with patch('src.spoofer.arp_spoofer.scapy.srp') as mock_srp:
        mock_response = MagicMock()
        mock_response.__getitem__.return_value = MagicMock(hwsrc="00:11:22:33:44:55")
        mock_srp.return_value = ([mock_response], None)
        
        mac = spoofer.get_mac("192.168.1.10")
        assert mac == "00:11:22:33:44:55"

def test_get_mac_invalid_ip(spoofer):
    with patch('src.spoofer.arp_spoofer.validate_ip', return_value=False):
        with pytest.raises(NetworkException, match="Invalid IP address: 256.256.256.256"):
            spoofer.get_mac("256.256.256.256")

def test_spoof(spoofer):
    with patch.object(spoofer, 'get_mac', return_value="00:11:22:33:44:55"):
        with patch('src.spoofer.arp_spoofer.scapy.sendp') as mock_sendp:
            spoofer.spoof("192.168.1.10", "192.168.1.1")
            assert mock_sendp.called

def test_restore(spoofer):
    with patch.object(spoofer, 'get_mac', return_value="00:11:22:33:44:55"):
        with patch('src.spoofer.arp_spoofer.scapy.sendp') as mock_sendp:
            spoofer.restore("192.168.1.10", "192.168.1.1")
            assert mock_sendp.called

def test_save_captured_data_txt(spoofer):
    spoofer.captured_packets = [
        MagicMock(time="2023-01-01T00:00:00", src="192.168.1.10", dst="192.168.1.1", payload="test payload")
    ]
    with patch('builtins.open', new_callable=MagicMock) as mock_open:
        spoofer.save_captured_data(format="txt")
        mock_open.assert_called_once()