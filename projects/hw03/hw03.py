LAB_SOURCE_FILE=__file__


HW_SOURCE_FILE=__file__


def num_eights(n):
    """Returns the number of times 8 appears as a digit of n.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> num_eights(8782089)
    3
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    def is_eight(digit):
        assert 0 <= digit < 10, "Only judge one-digit num!"
        if digit == 8:
            return 1
        else:
            return 0    
    if n < 10:
        return is_eight(n)
    else:
        return num_eights(n // 10) + is_eight(n % 10)


def digit_distance(n):
    """Determines the digit distance of n.

    >>> digit_distance(3)
    0
    >>> digit_distance(777)
    0
    >>> digit_distance(314)
    5
    >>> digit_distance(31415926535)
    32
    >>> digit_distance(3464660003)
    16
    >>> from construct_check import check
    >>> # ban all loops
    >>> check(HW_SOURCE_FILE, 'digit_distance',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n < 10:
        return 0
    else:
        last, last_but_one = n % 10, (n % 100) // 10
        diff = abs(last - last_but_one)
        return digit_distance(n // 10) + diff

def interleaved_sum(n, odd_func, even_func):
    """Compute the sum odd_func(1) + even_func(2) + odd_func(3) + ..., up
    to n.

    >>> identity = lambda x: x
    >>> square = lambda x: x * x
    >>> triple = lambda x: x * 3
    >>> interleaved_sum(5, identity, square) # 1   + 2*2 + 3   + 4*4 + 5
    29
    >>> interleaved_sum(5, square, identity) # 1*1 + 2   + 3*3 + 4   + 5*5
    41
    >>> interleaved_sum(4, triple, square)   # 1*3 + 2*2 + 3*3 + 4*4
    32
    >>> interleaved_sum(4, square, triple)   # 1*1 + 2*3 + 3*3 + 4*3
    28
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'interleaved_sum', ['While', 'For', 'Mod']) # ban loops and %
    True
    """
    "*** YOUR CODE HERE ***"
    def is_odd(x):
        if x == 1:
            return True
        else:
            return is_even(x-1)
        
    def is_even(x):
        if x == 1:
            return False
        else:
            return is_odd(x-1)
         
    if n == 1:
        return odd_func(1)
    elif is_odd(n):
        return interleaved_sum(n-1, odd_func, even_func) + odd_func(n)
    elif is_even(n):
        return interleaved_sum(n-1, odd_func, even_func) + even_func(n)


def next_larger_coin(coin):
    """Returns the next larger coin in order.
    >>> next_larger_coin(1)
    5
    >>> next_larger_coin(5)
    10
    >>> next_larger_coin(10)
    25
    >>> next_larger_coin(2) # Other values return None
    """
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25

def next_smaller_coin(coin):
    """Returns the next smaller coin in order.
    >>> next_smaller_coin(25)
    10
    >>> next_smaller_coin(10)
    5
    >>> next_smaller_coin(5)
    1
    >>> next_smaller_coin(2) # Other values return None
    """
    if coin == 25:
        return 10
    elif coin == 10:
        return 5
    elif coin == 5:
        return 1

def rec_next_sml(coin):
        if 1 < coin < 5:
            return 1
        elif coin <= 1:
            return 0
        elif coin > 25:
            return 25
        elif not next_smaller_coin(coin):
            return rec_next_sml(coin + 1)
        else:
            return next_smaller_coin(coin)

def count_coins(total):
    """Return the number of ways to make change using coins of value of 1, 5, 10, 25.
    >>> count_coins(15)
    6
    >>> count_coins(10)
    4
    >>> count_coins(20)
    9
    >>> count_coins(100) # How many ways to make change for a dollar?
    242
    >>> count_coins(200)
    1463
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'count_coins', ['While', 'For'])
    True
    """
    "*** YOUR CODE HERE ***"
    def helper(total, m):
        if total == 0:
            return 1
        elif total < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return helper(total - m, m) + helper(total, rec_next_sml(m))
    return helper(total, rec_next_sml(total+1))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if n == 1:
        print_move(start, end)
    else:
        other = 6 - start - end
        move_stack(n-1, start, other)
        move_stack(1, start, end)
        move_stack(n-1, other, end)



# This question use a concept named Y-combinator.
# One interested in it can view 
# https://stackoverflow.com/questions/1203292/recursive-lambda-expressions-possible or
# https://zhuanlan.zhihu.com/p/262284625
from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    >>> from construct_check import check
    >>> # ban any assignments or recursion
    >>> check(HW_SOURCE_FILE, 'make_anonymous_factorial',
    ...     ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr', 'FunctionDef', 'Recursion'])
    True
    """
    return (lambda z: (lambda x: z(lambda *args: (x(x))(*args)))(lambda x: z(lambda *args: (x(x))(*args))))(
            (lambda f: lambda x: 1 if x == 0 else mul(x, f(sub(x, 1))))
            )

    # if you want to know the detail of this complicate lambda function, you can see
    # my summary document of recursion, which also contains some my consideration of
    # recrsion.


