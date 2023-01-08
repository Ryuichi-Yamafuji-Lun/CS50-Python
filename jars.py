#implementation of jars exercise
class jar:
    def __init__(self, capacity = 12):
        if capacity < 1:
            raise ValueError
        self.capacity = capacity
        self.size = 0
    def __str__(self):
        cookie = ""
        while x < self.size:
            cookie += "🍪"
            x += 1
        return cookie
    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Too many cookies")
        else:
            self.size += n
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        else:
            self.size -= n
    @property
    def capacity(self):
        return self.capacity
    @property
    def size(self):
        return self.size