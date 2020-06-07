# pylint:disable=invalid-name
import operator


def bsearch(array, item, reverse=False):
    """Binary search on sorted arrays

    reverse=False, ascending order
    reverse=True, descending order
    """
    cmp = operator.gt if reverse else operator.lt

    L = 0
    R = len(array) - 1
    while L <= R:
        m = L + (R - L) // 2
        if array[m] == item:
            return m
        if cmp(array[m], item):
            L = m + 1
        else:
            R = m - 1
    return -1
