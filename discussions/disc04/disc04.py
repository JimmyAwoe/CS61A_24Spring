# Q1 Insect Combinatorics
def paths(height, width):
    """
    >>> paths(2, 2)
    2
    >>> paths(3, 3)
    6
    """
    if height == 1 or width == 1:
        return 1
    else:
        return paths(height - 1, width) + paths(height, width - 1)

# Q2 Max Product
def max_product(s):
    """
    >>> max_product([1, 2, 3])
    3
    >>> max_product([1, 6, 7, 2, 4])
    28
    """
    assert len(s) > 2, "No non-consecutive integer"
    if len(s) == 3:
        return s[0] * s[2]
    else:
        f = max([s[0] * x for x in s[2:]])
        step = max_product(s[1:])
        return max(f, step)
    

# Q3 Sum Fun
def sums(n, m):
    """
    >>> sums(2, 2)
    [[2]]
    >>> sums(5, 3)
    [[1, 3, 1], [2, 1, 2], [2, 3], [3, 2]]
    """
    if n == 1:
        return [[1]]
    elif n == 0:
        return [[]]
    else:
        sums_res = []
        for k in range(1, min(m, n) + 1):
            sums_res += [[k] + s for s in sums(n - k, m) if len(s) == 0 or s[0] != k]
        return  sums_res 
