class NodeList:
    def __init__(self, value):
        self.structure = [value, None, None]

    def __str__(self):
        return f'Value: {self.structure[0]}; left: {self.self.structure[1] != None}; right: {self.self.structure[2] != None}'

    def data(self):
        return self.structure[0]

    def left(self):
        return self.structure[1]

    def right(self):
        return self.structure[2]

    def list(self):
        kids = [x.list() if x is not None else x for x in self.structure[1::]]
        return [self.structure[0]] + kids
