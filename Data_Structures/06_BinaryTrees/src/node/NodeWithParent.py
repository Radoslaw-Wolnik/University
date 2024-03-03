class NodeWithParent(object):
    def __init__(self, data, parent):
        self.right = None
        self.left = None
        self.parent = parent
        self.data = data
    def __str__(self):
        return f'parent: {str(self.parent)},\n data: {self.data}, left: {True if self.left != None else False}, right: {True if self.left != None else False}'
