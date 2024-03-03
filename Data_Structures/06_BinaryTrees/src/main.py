from src.node.Node import Node
from src.node.NodeList import NodeList

from src.BinaryTree import BinaryTree
from src.BinaryTreeStackHelp import BinaryTreeStackHelp
from src.BinaryTreeNodeList import BinaryTreeNodeList
from src.BinaryTreeComplete import BinaryTreeComplete


if __name__ == "__main__":

    print("\n\n")
    print("binary trees")
    ### Building tree by hand
    #      1
    #     / \
    #   2   3
    #  / \  /\
    # 4  5 6  7
    #     \
    #      8
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.left.right.right = Node(8)

    print(tree.print_tree("preorder"))
    print(tree.print_tree("inorder"))
    print(tree.print_tree("postorder"))

    print("\n\n")
    print("STACK used to help print tree")
    ### Budujemy ręcznie drzewo
    #      1
    #     / \
    #   2   3
    #  / \  /\
    # 4  5 6  7
    #     \
    #      8
    tree_stack = BinaryTreeStackHelp(1)
    tree_stack.root.left = Node(2)
    tree_stack.root.right = Node(3)
    tree_stack.root.left.left = Node(4)
    tree_stack.root.left.right = Node(5)
    tree_stack.root.right.left = Node(6)
    tree_stack.root.right.right = Node(7)
    tree_stack.root.left.right.right = Node(8)

    print(tree_stack.print_tree("preorder"))
    print(tree_stack.print_tree("inorder"))
    print(tree_stack.print_tree("postorder"))

    print("\n\n")
    print("Binary tree with nodes implemented using list")
    ### Budujemy ręcznie drzewo with a list node
    #      1
    #     / \
    #   2   3
    #  / \  /\
    # 4  5 6  7
    #     \
    #      8
    tree_list = BinaryTreeNodeList(1)
    tree_list.root = NodeList(1)
    tree_list.root.structure[1] = NodeList(2)
    tree_list.root.structure[2] = NodeList(3)
    tree_list.root.structure[1].structure[1] = NodeList(4)
    tree_list.root.structure[1].structure[2] = NodeList(5)
    tree_list.root.structure[1].structure[2].structure[2] = NodeList(8)
    tree_list.root.structure[2].structure[1] = NodeList(6)
    tree_list.root.structure[2].structure[2] = NodeList(7)

    print(tree_list.preorder_print(tree_list.root, "")[:-1])
    print(tree_list.inorder_print(tree_list.root, "")[:-1])
    print(tree_list.postorder_print(tree_list.root, "")[:-1])
    print(tree_list.list())



    # Copmplete tree with height and counting
    print("\n\n")
    print("Complete tree")

    ### Budujemy ręcznie drzewo
    #       1
    #     /  \
    #   2     3
    #  / \   /
    # 4  5  6
    #     \
    #      8
    tree_c = BinaryTreeComplete(1)
    tree_c.root.left = Node(2)
    tree_c.root.right = Node(3)
    tree_c.root.left.left = Node(4)
    tree_c.root.left.right = Node(5)
    tree_c.root.right.left = Node(6)
    tree_c.root.left.right.right = Node(8)

    print(tree_c.print_tree("preorder"))
    print(tree_c.print_tree("inorder"))
    print(tree_c.print_tree("postorder"))
    print(tree_c.Height(tree_c.root))
    print(tree_c.CountLeaves(tree_c.root))
    print(tree_c.CountNodes(tree_c.root))

    Test = BinaryTreeComplete(10)
    Test.root.left = Node(2)
    Test.root.right = Node(3)
    Test.root.left.left = Node(4)
    Test.root.right.left = Node(5)
    Test.root.left.left.right = Node(6)
    Test.root.left.left.right.right = Node(8)
    Test.root.left.left.right.right.left = Node(0)
    print(Test.print_tree("preorder"))
    print(Test.print_tree("inorder"))
    print(Test.print_tree("postorder"))
    print(Test.Height(Test.root))
    print(Test.CountLeaves(Test.root))
    print(Test.CountNodes(Test.root))
