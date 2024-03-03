class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f'value: {self.value}; left: {self.left != None}; right: {self.right != None}'
