#implementation of jars exercise
class jar:
    def __init__(self, capacity = 12):
        if capacity < 1:
            raise ValueError
        self._capacity = capacity
        self._size = 0
    def __str__(self):
        return self.size * "🍪"
    def deposit(self, n):
        if self.size + n > self._capacity:
            raise ValueError("Too many cookies")
        else:
            self._size += n
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Not enough cookies")
        else:
            self._size -= n
    @property
    def capacity(self):
        return self._capacity
    @property
    def size(self):
        return self._size

def main():
    jars = jar()
    jars.deposit(10)
    jars.withdraw(5)
    print(jars)

if __name__ == "__main__":
    main()