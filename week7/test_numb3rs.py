from numb3rs import validate

def test_validate():
    assert validate("1.1.1") == False
    assert validate("cat") == False
    assert validate("275.3.6.28") == False
    assert validate("1.1.1.1") == True
    assert validate("217.0.0.1") == True
