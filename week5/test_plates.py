from plates import is_valid

def test_is_valid():
    assert is_valid("CS50") == 1
    assert is_valid("CS05") == 0
    assert is_valid("CS50P") == 0
    assert is_valid("PI3.14") == 0
    assert is_valid("H") == 0
    assert is_valid("OUTATIME") == 0