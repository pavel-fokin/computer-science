from cs.permutations import lexicographic


def test_next_lex():
    assert lexicographic([1, 2]) == [2, 1]
    assert lexicographic([1, 2, 3]) == [1, 3, 2]
    assert lexicographic([3, 2, 1]) == [1, 2, 3]
    assert lexicographic([1, 1, 5]) == [1, 5, 1]
    assert lexicographic([1, 3, 2]) == [2, 1, 3]
