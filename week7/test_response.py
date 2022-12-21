from response import valid

def test_valid():
    assert valid("malan") == "Invalid"
    assert valid("malan at harvard dot edu") == "Invalid"
    assert valid("malan@harvard.edu") == "Valid"