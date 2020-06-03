class Trie:

    def __init__(self):
        self.children = {}
        self.value = None

    def insert(self, key: str, value=True):
        node = self
        for char in key:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.value = value

    def find(self, key: str):
        node = self
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.value

    def all_words(self):
        for char, child in self.children.items():
            if child.value:
                yield f"{char}"
            else:
                for each in child.all_words():
                    yield char + each
