# reprezentacje ósemkowe liczb naturalnych od 0 do n
class RangeBase8:
    '''range(n) in base 8'''

    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            buff = self.i
            self.i += 1

            if buff == 0:
                return buff

            temp = []
            while buff > 0:
                temp.append(str(buff - (buff // 8) * 8))
                buff = int(buff / 8)
            return ''.join(temp)

        else:
            raise StopIteration
