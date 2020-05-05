class Trie:
    class Node:
        def __init__(self):
            self.children = {}
            self.value = None

    def __init__(self):
        self.root = Trie.Node()

    def insert(self, key: str, value=True):
        node = self.root
        for char in key:
            if char not in node.children:
                node.children[char] = Trie.Node()
            node = node.children[char]
        node.value = value

    def find(self, key: str):
        node = self.root
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value
