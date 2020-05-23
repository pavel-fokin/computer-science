from cs.permutations import heaps, lexicographic


def test_next_lex():
    expected = [
        [1, 2, 3],
        [1, 3, 2],
        [2, 1, 3],
        [2, 3, 1],
        [3, 1, 2],
        [3, 2, 1],
    ]
    assert expected == list(lexicographic([1, 2, 3]))


def test_heaps_algorithm():
    expected = [
        [1, 2, 3],
        [2, 1, 3],
        [3, 2, 1],
        [2, 3, 1],
        [1, 2, 3],
        [2, 1, 3],
    ]
    assert expected == list(heaps([1, 2, 3]))
