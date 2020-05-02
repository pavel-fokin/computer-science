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


def selection(array: list, reverse=False) -> list:

    def find(array, cmp):
        """Find index of min or max element."""
        idx = 0
        for i in range(1, len(array)):
            if cmp(array[idx], array[i]):
                idx = i
        return idx

    cmp = operator.lt if reverse else operator.gt
    n = len(array)  # pylint:disable=invalid-name

    for i in range(n):
        index = find(array[i:], cmp)
        array.insert(i, array[i + index])
        array.pop(i + index + 1)

    return array


def merge(array: list, reverse=False) -> list:

    def merge_sorted(left, right, cmp):
        merged = []
        l, r = len(left), len(right)  # pylint:disable=invalid-name
        i = j = 0

        while i < l and j < r:
            if cmp(left[i], right[j]):
                merged.append(right[j])
                j += 1
            else:
                merged.append(left[i])
                i += 1

        if i < l:
            tail = left[i:]
        elif j < r:
            tail = right[j:]
        else:
            tail = []

        return merged + tail

    def sort_(array, cmp):
        n = len(array)  # pylint:disable=invalid-name

        if n < 2:
            return array

        middle = n // 2
        left = sort_(array[:middle], cmp)
        right = sort_(array[middle:], cmp)

        return merge_sorted(left, right, cmp)

    cmp = operator.lt if reverse else operator.gt
    return sort_(array, cmp)


def quick(array: list, reverse=False) -> list:
    def sort_(array, cmp):
        if array == []:
            return []
        pivot = array[0]
        left = [x for x in array[1:] if cmp(array[0], x)]
        right = [x for x in array[1:] if not cmp(array[0], x)]
        return sort_(left, cmp) + [pivot] + sort_(right, cmp)

    cmp = operator.le if reverse else operator.ge
    return sort_(array, cmp)
