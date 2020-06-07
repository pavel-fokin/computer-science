import pytest

from cs.trie import Trie


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

    assert sorted(list(trie.all_words())) == sorted(["hot", "dog", "hit"])


def test_find_pattern():
    trie = Trie()
    trie.insert("hot")
    trie.insert("dog")
    trie.insert("hit")

    assert trie.find_pattern("h.t")
    assert trie.find_pattern("..t")
    assert not trie.find_pattern("..x")


@pytest.mark.xfail
def test_find_pattern_case2():
    trie = Trie()
    trie.insert("a")

    assert trie.find("a")
    assert trie.find(".")
    assert not trie.find(".a")
    assert not trie.find("a.")
