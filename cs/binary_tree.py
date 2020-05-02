class BinaryTree:
    class Node:
        def __init__(self, data, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

        def add_left(self, data):
            if self.left is not None:
                raise RuntimeError
            self.left = BinaryTree.Node(data)

        def add_right(self, data):
            if self.right is not None:
                raise RuntimeError
            self.right = BinaryTree.Node(data)

        def is_empty(self):
            return (
                self.data is None
                and self.left is None
                and self.right is None
            )

    def __init__(self, data=None):
        if data is None:
            self.root = None
        else:
            self.root = BinaryTree.Node(data)

    def is_empty(self):
        return self.root is None or self.root.is_empty()


class Inorder:
    """Left -> Root -> Right"""

    def __init__(self, binary_tree):
        self.binary_tree = binary_tree

    @staticmethod
    def traverse(root):
        if root:
            yield from Preorder.traverse(root.left)
            yield root
            yield from Preorder.traverse(root.right)

    def __iter__(self):
        return Inorder.traverse(self.binary_tree.root)


class Preorder:
    """Root -> Left -> Right"""

    def __init__(self, binary_tree):
        self.binary_tree = binary_tree

    @staticmethod
    def traverse(root):
        if root:
            yield root
            yield from Preorder.traverse(root.left)
            yield from Preorder.traverse(root.right)

    def __iter__(self):
        return Preorder.traverse(self.binary_tree.root)


class Postorder:
    """Left -> Right -> Root"""

    def __init__(self, binary_tree):
        self.binary_tree = binary_tree

    @staticmethod
    def traverse(root):
        if root:
            yield from Postorder.traverse(root.left)
            yield from Postorder.traverse(root.right)
            yield root

    def __iter__(self):
        return Postorder.traverse(self.binary_tree.root)
