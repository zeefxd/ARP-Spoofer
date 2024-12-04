from src.utils.validators import validate_ip

def test_validate_ip_valid():
    assert validate_ip('192.168.1.1') == True
    assert validate_ip('10.0.0.1') == True

def test_validate_ip_invalid():
    assert validate_ip('256.256.256.256') == False
    assert validate_ip('invalid_ip') == False