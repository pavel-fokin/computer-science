from cs.trie import Trie


def test_trie():
    trie1 = Trie()
    trie1.insert("bad")
    assert trie1.find("bad")

    assert trie1.find("add") is None

    trie1.insert("add")
    assert trie1.find("add")
