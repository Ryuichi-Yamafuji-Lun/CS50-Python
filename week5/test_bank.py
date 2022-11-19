#unit test bank.py
from bank import amount

def test_amount():
    assert amount("hello") == 0
    assert amount("Hello") == 0
    assert amount("Hello, John") == 0
    assert amount("Hey, John") == 20
    assert amount("Whats up bro!") == 100