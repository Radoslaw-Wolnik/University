class Stack:
    def __init__(self):
        self.start()

    def start(self):
        self.structure = []

    def push(self, val):
        self.structure.append(val)

    def pop(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.structure.pop()

    def peak(self):
        if self.isEmpty():
            return 'Stack is empty'
        return self.structure[-1]

    def __str__(self):
        temp = [str(x) for x in self.structure]
        return str(temp)

    def isEmpty(self):
        return len(self.structure) == 0
