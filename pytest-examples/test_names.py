from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

def test_make_full_name():
    assert make_full_name("Sally-bordon", "Brown") == "Brown; Sally-bordon"
    assert make_full_name("John", "Doe") == "Doe; John"
    assert make_full_name("", "") == "; "
    assert make_full_name("Sally", "") == "; Sally"
    assert make_full_name("", "Brown") == "Brown; "
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("John", "Doe") == "Doe; John"
#pytest.main(["-v", "--tb=line", "-rN", __file__])
def test_extract_family_name():
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
    assert extract_family_name("; Sally") == ""
    assert extract_family_name("Brown; ") == "Brown"
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Doe; John") == "Doe"
#pytest.main(["-v", "--tb=line", "-rN", __file__])
def test_extract_given_name():
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; John") == "John"
    assert extract_given_name("; Sally") == "Sally"
    assert extract_given_name("Brown; ") == ""
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("Doe; John") == "John"
pytest.main(["-v", "--tb=line", "-rN", __file__])
    