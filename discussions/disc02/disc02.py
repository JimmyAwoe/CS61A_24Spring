# Q1 Warm Up
# Ans: 30

# Q2 Make Keeper
def make_keeper(n):
    def f(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i, end='\n')
            i += 1
    return f

# Q3 Digit Finder
def find_digit(k):
    def f(x):
        return (x // 10 ** (k - 1)) % 10
    return f

# Q4 Match Maker
def match_k(k):
    """
    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(3)(200200)
    True
    >>> match_k(5)(153411534115341)
    True
    >>> match_k(4)(238423812381)
    False
    """
    def f(x):
        digit = 1
        while x // 10 ** (digit + k - 1) != 0:
            if find_digit(digit+k)(x) != find_digit(digit)(x):
                return False
            digit += 1
        return True
    return f