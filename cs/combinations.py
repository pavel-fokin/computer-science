def combinations(array, n):
    for i in range(len(array)):
        if n == 1:
            yield [array[i]]
        for each in combinations(array[i + 1:], n - 1):
            yield [array[i]] + each


def combinations2(n, k):
    for i in range(1, n + 1):
        if k == 1:
            yield [i]
        for each in combinations2(n - i, k - 1):
            yield [i] + each
