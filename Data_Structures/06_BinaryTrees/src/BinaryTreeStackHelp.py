from src.stack.Stack import Stack
from src.node.Node import Node


class BinaryTreeStackHelp(object):
    def __init__(self, root):
        self.root = Node(root)

    # funkcja pomocnicza do wyświetlania drzewa

    def print_tree(self, visit_type):
        if visit_type == "preorder":
            return self.preorder_print(self.root)
        elif visit_type == "inorder":
            return self.inorder_print(self.root)
        elif visit_type == "postorder":
            return self.postorder_print(self.root)
        else:
            print("visit type " + str(visit_type) + " brak metody.")
            return False

    def preorder_print(self, tree):
        """print curr val, check out left, check out right"""
        res = []
        stosik = Stack()
        stosik.push(tree)
        while stosik.isEmpty() == False:
            nowTree = stosik.pop()
            res.append(str(nowTree.value))
            if nowTree.right != None:
                stosik.push(nowTree.right)
            if nowTree.left != None:
                stosik.push(nowTree.left)
        return '-'.join(res)

    def inorder_print(self, tree):
        """check out left, print curr val, check out right"""
        current = tree
        stosik = Stack()
        res = []
        while True:
            # print(stosik)
            # Reach the left most Node of the current Node
            if current is not None:
                # Place pointer to a tree node on the stack
                # before traversing the node's left subtree
                stosik.push(current)
                current = current.left
            # BackTrack from the empty subtree and visit the Node
            # at the top of the stack; however, if the stack is
            # empty you are done
            elif (stosik.isEmpty() == False):
                current = stosik.pop()
                res.append(str(current.value))
                # We have visited the node and its left
                # subtree. Now, it's right subtree's turn
                current = current.right
            else:
                break
        return "-".join(res)

    def postorder_print(self, tree):
        """check out left, check out right, print curr val"""
        res = []
        stack = Stack()
        while (True):
            while (tree):
                # Push root's right child and then root to stack
                if tree.right is not None:
                    stack.push(tree.right)
                stack.push(tree)

                # Set root as root's left child
                tree = tree.left

            # Pop an item from stack and set it as root
            tree = stack.pop()

            # If the popped item has a right child and the
            # right child is not processed yet, then make sure
            # right child is processed before root
            if (tree.right is not None and stack.peak() == tree.right):
                stack.pop()  # Remove right child from stack
                stack.push(tree)  # Push root back to stack
                tree = tree.right  # change root so that the
                # right childis processed next

            # Else print root's data and set root as None
            else:
                res.append(str(tree.value))
                tree = None

            if stack.isEmpty() == True:
                break
        return '-'.join(res)