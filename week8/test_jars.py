from jars import jar

def test_jar():
    Jar = jar()
    assert str(Jar) == ""
    Jar.deposit(5)
    assert str(Jar) == "🍪🍪🍪🍪🍪"
    Jar.withdraw(2)
    assert str(Jar) == "🍪🍪🍪"