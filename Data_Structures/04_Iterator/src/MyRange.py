# iterator
# protokół __iter__
# protokół __next__
# <podnosi StopIteration>

class MyRange():
    '''range(n)'''

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            buff = self.i
            self.i += 1
            return buff
        else:
            raise StopIteration
