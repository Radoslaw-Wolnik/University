class Stack:
    def __init__(self):
        self.structure = []

    def add(self, val):
        assert isinstance(val, (str, int, float)), "This element can't be in Stack\nU can add str, int or float"
        self.structure.append(val)

    def get(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.structure.pop()

    def peak(self):
        if self.is_empty():
            return 'Stack is empty'
        return self.structure[-1]

    def __str__(self):
        return str(self.structure)

    def is_empty(self):
        if len(self.structure) == 0:
            return True
        else:
            return False
