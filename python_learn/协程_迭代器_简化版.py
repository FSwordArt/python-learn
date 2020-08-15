import time
from collections.abc import Iterable
from collections.abc import Iterator

class Classmate(object):

    def __init__(self):
        self.names = list()
        self.index = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        return self

    def __next__(self):

        if self.index < len(self.names):
            set = self.names[self.index]
            self.index += 1
            return set

        else:
            raise StopIteration


classmate = Classmate()
classmate.add("11")
classmate.add("22")
classmate.add("33")

for name in classmate:

    print(name)
    time.sleep(1)