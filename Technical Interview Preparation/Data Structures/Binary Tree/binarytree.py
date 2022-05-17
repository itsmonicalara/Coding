class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self):
        self.root = None

    def print_tree(self):
        print(self.data)

tree = Tree()
tree.root = Node(10)
tree.root.left = Node(15)
tree.root.right = Node(35)
tree.print_tree()
