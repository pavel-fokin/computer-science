from sort import bubble, insertion, merge, quick, selection


def test_sort_success(method):
    res = method([5, 4, 3, 2, 1])
    assert res == [1, 2, 3, 4, 5], res

    res = method([5, 5, 2, 3, 1])
    assert res == [1, 2, 3, 5, 5], res


def test_sort_reverse(method):
    res = method([1, 2, 3, 4, 5], reverse=True)
    assert res == [5, 4, 3, 2, 1], res


def test_sort_equal(method):
    assert method([1, 1, 1, 1]) == [1, 1, 1, 1]


def test_sort_one(method):
    assert method([1]) == [1]


def test_sort_empty(method):
    assert method([]) == []


for method in (bubble, insertion, selection, merge, quick):
    test_sort_success(method)
    test_sort_reverse(method)
    test_sort_empty(method)
    test_sort_one(method)
