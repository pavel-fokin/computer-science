import operator


def bubble(array: list, reverse=False) -> list:
    cmp = operator.lt if reverse else operator.gt
    n = len(array)  # pylint:disable=invalid-name
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if cmp(array[i-1], array[i]):
                array[i-1], array[i] = array[i], array[i-1]
                swapped = True
    return array


def insertion(array: list, reverse=False) -> list:
    cmp = operator.lt if reverse else operator.gt
    n = len(array)  # pylint:disable=invalid-name
    for i in range(n+1):
        for j in reversed(range(1, i)):
            if cmp(array[j-1], array[j]):
                array[j-1], array[j] = array[j], array[j-1]
    return array
