class Trie:
    def __init__(self):
        self.children = {}
        self.is_word = None

    def insert(self, key: str, is_word=True):
        node = self
        for char in key:
            if char not in node.children:
                node.children[char] = Trie()
            node = node.children[char]
        node.is_word = is_word

    def find(self, key: str):
        node = self
        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None
        return node.is_word

    def find_pattern(self, pattern: str) -> bool:
        """Find given pattern in a Trie.

        Letter in a word can be replaced with a '.'
        """

        if not pattern and self.is_word:
            return True

        node = self
        for i, char in enumerate(pattern):
            if char == ".":
                res = []
                for each in node.children.values():
                    res.append(each.find_pattern(pattern[i + 1:]))
                return any(res)

            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.is_word

    def all_words(self):
        """Iterate through all words in Trie."""

        for char, child in self.children.items():
            if child.is_word:
                yield f"{char}"
            else:
                for each in child.all_words():
                    yield char + each
