# Q1
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

next(filter(lambda n: n > 2024, gen_fib()))

# Q2
def differences(t):
    previous_x = next(t)
    for x in t:
        yield x - previous_x
        previous_x = x


# Q3
def partition_gen(n, m):
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in partition_gen(n-m, m):
            yield str(p) + ' + ' + str(m)
        yield from partition_gen(n, m-1)
    