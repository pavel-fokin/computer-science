from binary_tree import BinaryTree, Preorder, Inorder, Postorder


def test_init_binary_tree():
    bt1 = BinaryTree()
    assert bt1.is_empty()

    bt2 = BinaryTree(1)
    assert not bt2.is_empty()
    assert bt2.root.data == 1


def test_node_add_left():
    root = BinaryTree.Node(1)
    root.add_left(2)
    assert root.left.data == 2


def test_node_add_right():
    root = BinaryTree.Node(1)
    root.add_right(3)
    assert root.right.data == 3


def test_preorder_traverse():
    tree = BinaryTree(1)
    tree.root.add_left(2)
    tree.root.add_right(3)

    traverse = Preorder(tree)

    assert [node.data for node in traverse] == [1, 2, 3]


def test_inorder_traverse():
    tree = BinaryTree(1)
    tree.root.add_left(2)
    tree.root.add_right(3)

    traverse = Inorder(tree)

    assert [node.data for node in traverse] == [2, 1, 3]


def test_postorder_traverse():
    tree = BinaryTree(1)
    tree.root.add_left(2)
    tree.root.add_right(3)

    traverse = Postorder(tree)

    assert [node.data for node in traverse] == [2, 3, 1]


if __name__ == '__main__':
    test_init_binary_tree()
    test_node_add_left()
    test_node_add_right()

    test_preorder_traverse()
    test_inorder_traverse()
    test_postorder_traverse()
    print("Test BinaryTree :: OK")

