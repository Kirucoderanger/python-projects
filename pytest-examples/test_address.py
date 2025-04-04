from address import extract_city, extract_state, extract_zipcode
import pytest

def test_extract_city():
    assert extract_city("525 S Center St, Rexburg, ID 83460") == "Rexburg"
    assert extract_state("525 S Center St, Rexburg, ID 83460") == "ID"
    assert extract_zipcode("525 S Center St, Rexburg, ID 83460") == "83460"
pytest.main(["-v", "--tb=line", "-rN", __file__])
