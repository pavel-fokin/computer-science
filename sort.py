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
