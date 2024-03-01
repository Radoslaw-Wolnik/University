class StackKind:
    def __init__(self, kind):
        self.kind = None
        self.set_kind(kind)
        self.structure = []
        
    def set_kind(self, kind):
        assert kind in ['beginning',
                        'ending'], f'There is no such a kind of stack as {kind}\nChose from: ["beginning", "ending"]'
        if kind == 'beginning':
            self.kind = False
        if kind == 'ending':
            self.kind = True

    def get_kind(self):
        return self.kind

    def add(self, val):
        assert isinstance(val, (str, int, float)), "This element can't be in Stack\nU can add str, int or float"
        if self.get_kind():
            self.structure.append(val)
        else:
            self.structure.insert(0, val)

    def get(self):
        if self.structure == []:
            return 'Stack is empty'
        if self.get_kind():
            return self.structure.pop(-1)
        else:
            return self.structure.pop(0)

    def __str__(self):
        return str(self.structure)
    