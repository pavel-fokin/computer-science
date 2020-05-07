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

    l = 0
    for i in reversed(range(k, n)):
        if array[i] > array[k]:
            l = i
            break

    array[l], array[k] = array[k], array[l]

    array[k+1:] = array[k+1:][::-1]

    return array
