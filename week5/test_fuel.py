#unit test fuel.py
from fuel import gauge, convert
import pytest

def test_convert():
    assert convert("0/7") == 0
    assert convert("3/4") == 75
    with pytest.raises(ZeroDivisionError):
        0/0
    with pytest.raises(ValueError):
        1.5/3
    with pytest.raises(ValueError):
        "three/four"

def test_gauge():
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
