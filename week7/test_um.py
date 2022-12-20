from um import count

def test_count():
    assert count("um...") == 1
    assert count("yummy") == 0
    assert count("yum") == 0
    assert count("hello, um, world") == 1
    assert count("um, hello, um, world") == 2
    