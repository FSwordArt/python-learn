from collections.abc import Iterator
from collections.abc import Iterable

class Fabonacci(object):

    def __init__(self, all_num):
        
        self.all_num = all_num
        self.index = 0
        self.a = 0
        self.b = 1

    def __iter__(self):

        return self

    def __next__(self):

        if self.index < self.all_num:

            set = self.a
            self.a, self.b = self.b, self.a + self.b
            self.index += 1

            return set

        else:
            raise StopIteration

fibo = Fabonacci(10)

for num in fibo:
    print(num)