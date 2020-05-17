def lexicographic(array):
    n = len(array)
    if n <= 1:
        return array

    k = -1
    for i in reversed(range(n-1)):
        if array[i] < array[i+1]:
            k = i
            break

    if k == -1:
        return array[::-1]

    l = n
    for i in reversed(range(k, n)):
        if array[i] > array[k]:
            l = i
            break

    array[l], array[k] = array[k], array[l]

    array[k+1:] = array[k+1:][::-1]

    return array


def _heaps_permutation(array, n):
    if n == 1:
        yield array
    else:
        yield from _heaps_permutation(array, n-1)
        for i in range(n-1):
            if i % 2 == 0:
                array[i], array[n-1] = array[n-1], array[i]
            else:
                array[0], array[n-1] = array[n-1], array[0]
            yield from _heaps_permutation(array, n-1)


def heaps(array):
    yield from _heaps_permutation(array, len(array))
