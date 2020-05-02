from sort import bubble


def test_sort_success():
    res = bubble([5, 4, 3, 2, 1])
    assert res == [1, 2, 3, 4, 5], res

    res = bubble([5, 5, 2, 3, 1])
    assert res == [1, 2, 3, 5, 5], res


def test_sort_reverse():
    res = bubble([1, 2, 3, 4, 5], reverse=True)
    assert res == [5, 4, 3, 2, 1], res


def test_sort_one():
    assert bubble([1]) == [1]


def test_sort_empty():
    assert bubble([]) == []


test_sort_success()
test_sort_reverse()
test_sort_empty()
