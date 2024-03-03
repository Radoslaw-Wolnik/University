from src.node.NodeList import NodeList


class BinaryTreeNodeList(object):
    def __init__(self, root):
        self.root = NodeList(root)

    def preorder_print(self, start, visit):
        """Root->Left->Right"""
        if start:
            print(start)
            visit += (str(start.data()) + "-")
            visit = self.preorder_print(start.left(), visit)
            visit = self.preorder_print(start.right(), visit)
        return visit

    def inorder_print(self, start, visit):
        if start:
            visit = self.inorder_print(start.left(), visit)
            visit += (str(start.data()) + "-")
            visit = self.inorder_print(start.right(), visit)
        return visit

    def postorder_print(self, start, visit):
        if start:
            visit = self.postorder_print(start.left(), visit)
            visit = self.postorder_print(start.right(), visit)
            visit += (str(start.data()) + "-")
        return visit

    def list(self):
        return self.root.list()
