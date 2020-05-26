from cs.trie import Trie, all_words


def test_trie_use_case():
    trie = Trie()
    trie.insert("bad")
    assert trie.find("bad")

    assert trie.find("add") is None

    trie.insert("add")
    assert trie.find("add")


def test_trie_empty():
    trie = Trie()
    assert trie.find("word") is None


def test_trie_insert():
    trie = Trie()
    trie.insert("word")
    trie.insert("wordwide")


def test_trie_all_words():
    trie = Trie()
    trie.insert("hot")
    trie.insert("dog")
    trie.insert("hit")

    assert sorted(list(all_words(trie))) == sorted(["hot", "dog", "hit"])
