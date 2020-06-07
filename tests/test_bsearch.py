from cs.bsearch import bsearch


def test_bsearch_asc():
    assert bsearch([1, 2, 3, 4], 1) == 0
    assert bsearch([1, 2, 3, 4], 3) == 2
    assert bsearch([1, 2, 3, 4], 4) == 3
    assert bsearch([1, 2, 3, 4, 5, 6], 2) == 1


def test_bsearch_desc():
    assert bsearch([4, 3, 2, 1], 4, reverse=True) == 0
    assert bsearch([4, 3, 2, 1], 3, reverse=True) == 1
    assert bsearch([4, 3, 2, 1], 1, reverse=True) == 3
    assert bsearch([6, 5, 4, 3, 2, 1], 2, reverse=True) == 4
