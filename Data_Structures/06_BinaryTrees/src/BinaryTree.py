from src.node.Node import Node


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # funkcja pomocnicza do wyświetlania drzewa

    def print_tree(self, visit_type):
        if visit_type == "preorder":
            return self.preorder_print(self.root, "")[:-1]
        elif visit_type == "inorder":
            return self.inorder_print(self.root, "")[:-1]
        elif visit_type == "postorder":
            return self.postorder_print(self.root, "")[:-1]
        else:
            print("visit type " + str(visit_type) + " brak metody.")
            return False

    #   root-left-right
    #   1-2-4-5-3
    def preorder_print(self, start, visit):
        """Root->Left->Right"""
        if start:
            visit += (str(start.value) + "-")
            visit = self.preorder_print(start.left, visit)
            visit = self.preorder_print(start.right, visit)
        return visit

    def inorder_print(self, start, visit):
        if start:
            visit = self.inorder_print(start.left, visit)
            visit += (str(start.value) + "-")
            visit = self.inorder_print(start.right, visit)
        return visit

    def postorder_print(self, start, visit):
        if start:
            visit = self.postorder_print(start.left, visit)
            visit = self.postorder_print(start.right, visit)
            visit += (str(start.value) + "-")
        return visit
