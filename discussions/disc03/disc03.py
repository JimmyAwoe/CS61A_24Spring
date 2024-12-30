# Q1
def split(n):
    return n // 10, n % 10


def swipe(n):
    """
    >>> swipe(32)
    2
    3
    2
    >>> swipe(102304)
    4
    0
    3
    2
    0
    1
    0
    2
    3
    0
    4
    """
    if n < 10:
        print(n)
    else:
        all_but_last, last = split(n)
        print(last)
        swipe(all_but_last)
        print(last)


# Q2
def skip_factorial(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    

# Q3
def is_prime(n):
    """
    >>> is_prime(169)
    False
    >>> is_prime(17)
    True
    """
    assert n > 1
    def helper(k):
        """recursively to identify if n can be integer divided by integer between k and n"""
        if n <= k:
            return True
        elif n % k == 0:
            return False
        else:
            return helper(k+1) 
    return helper(2)


# Q4
def rec_hailstone(n):
    """
    >>> rec_hailstone(4)
    4
    2
    1
    2
    """
    print(int(n))
    def helper(step):
        if n == 1:
            return 0
        elif is_odd(n):
            step = rec_hailstone(3 * n + 1) + 1
        elif is_even(n):
            step = rec_hailstone(n / 2) + 1
        return step 
    return helper(0)
    
def is_odd(k):
    if k == 1:
        return True
    else:
        return is_even(k - 1)
    
def is_even(k):
    if k == 1:
        return False
    else:
        return is_odd(k - 1)
    
    
# Q5
def sevens(n, k):
    """
    >>> sevens(20, 5)
    5
    >>> sevens(18, 5)
    2
    >>> sevens(2, 5)
    2
    >>> sevens(6, 5)
    1
    >>> sevens(7, 5)
    2
    >>> sevens(8, 5)
    1
    >>> sevens(9, 5)
    5
    """
    def is_seven(i):
        def digit_seven(i):
            if i < 10 and i % 10 != 7:
                return False
            elif i % 10 == 7:
                return True
            else:
                return digit_seven(i // 10)
            
        if i % 7 == 0 or digit_seven(i):
            return True
        else:
            return False

    def get_dire(i):
        dire = 1
        if i == 1:
            dire = 1
        elif is_seven(i-1):
            dire = get_dire(i - 1) * -1
        else:
            dire = get_dire(i - 1)
        return dire

    def advance(who, dire):
        if who + dire > k:
            return 1
        elif who + dire < 1:
            return 5
        else:
            return who + dire
        
    def helper():
        if n == 1:
            return 1
        else:
            dire = get_dire(n)
            who = advance(sevens(n - 1, k), dire)
            return who
    return helper()



# Q6
# To solve this question, we assume Karel start to face right.
# This assumption doesn't exist in the offical website of Karel or disc03.
# However, without this assumption, there would be no way to achieve the aim.
# This is because without that, Karel cann't know which direction is bettom.

# Here we first try to visualize the move process by defining the four function.
# This isn't necessary, but this make sure one can run main() directly without installing
# karel module, which help Python understand the code.
def move(coor, dire):
    print("from", coor, "->move")
    x, y = coor 
    if dire == "left":
        return (x-1, y)
    elif dire == "right":
        return (x+1, y)
    elif dire == "up":
        return (x, y+1)
    elif dire == "down":
        return (x, y-1)
    

def turn_left(dire):
    print("from", dire, "->turn left")
    if dire == "left":
        return "down"
    elif dire == "right":
        return "up"
    elif dire == "up":
        return "left"
    elif dire == "down":
        return "right"
    

def front_is_clear(coordinates, n, dire):
    x, y = coordinates
    if dire == "left":
        if x > 1:
            return True
        else:
            return False
    elif dire == "right":
        if x < n:
            return True
        else:
            return False
    elif dire == "up":
        if y < n:
            return True
        else:
            return False
    elif dire == "down":
        if y > 1:
            return True
        else:
            return False
        
def front_is_blocked(coordinates, n, dire):
    return not front_is_clear(coordinates, n, dire)


def main(start_coor, n):
    start_dire = "right"
    # Below is the body of the main()
    # First define some tool
    def turn_right(dire):
        return turn_left(turn_left(turn_left(dire)))
        

    def turn_around(dire):
        return turn_left(turn_left(dire))
    
    # define a safe move function to avoid error
    def smove(coor, n, dire):
        if front_is_clear(coor, n, dire):
            return move(coor, dire)
        else:
            return coor
        
    def leftup_to_rightdown(coor, n, dire):
        # we ask Karel to move twice left and once down
        coor = smove(coor, n, dire)
        coor = smove(coor, n, dire)
        dire = turn_right(dire)
        coor = smove(coor, n, dire)
        coor = smove(coor, n, dire)
        dire = turn_left(dire)
        return coor, dire

    def rightup_to_leftdown(coor, n, dire):
        # we ask Karel to move twice right and once down
        coor = smove(coor, n, dire)
        coor = smove(coor, n, dire)
        dire = turn_left(dire)
        coor = smove(coor, n, dire)
        coor = smove(coor, n, dire)
        dire = turn_right(dire)
        return coor, dire
    
    def to_middle_bottom(move_func, coor, n, dire):
        """
        This function ask Karel to stop in the middle of bottom line.
        """
        # Every time invoking front_is_clear would invoke rightup_to_right_down first.
        coor, dire = move_func(coor, n, dire)
        # When Karel doesn't reach the wall, continue this process, i.e., recursively call itself.
        if front_is_clear(coor, n, dire):
            coor, dire = to_middle_bottom(move_func, coor, n, dire)    
        else:
            dire = turn_around(dire)
        # Every time invoking front_is_clear would book a move back.
        coor = move(coor, dire)
        return coor, dire

    # if Karel begin in left corner
    if front_is_clear(start_coor, n, start_dire):
        return to_middle_bottom(leftup_to_rightdown, start_coor, n, start_dire)
    # if Karel begin in right corner
    else:
        start_dire = turn_around(start_dire)
        return to_middle_bottom(rightup_to_leftdown, start_coor, n, start_dire)




            