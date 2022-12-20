#test working.py
from working import convert

def test_convert():
    assert convert("9:00 AM to 3:00 PM") == "09:00 to 15:00"
    assert convert("3:00 PM to 9:00 AM") == "15:00 to 09:00"
    assert convert("9 AM to 3 PM") == "09:00 to 15:00"
    assert convert("9:30 AM to 3:45 PM") == "09:30 to 15:45"