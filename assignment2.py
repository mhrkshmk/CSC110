import doctest
def add_to_cart(price:int, total_price:int, balance:int) :
    """
    This function is a shopping cart, it gets the price of an item, total price of items already in the cart, and the money we can spend,
    all as an integer. If our total price is more than our balance after adding the new item, if will print not enough funds, You need an
    additional $ X, where X is the extra money we need to go shopping. Otherwise, it will print cart balance $ X, where X is the money we will
    have after buying the entire cart.
    >>> add_to_cart(10, 20, 25)
    not enough funds! You need an additional $ 5
    >>> add_to_cart(10, 20, 50)
    cart balance $ 30
    """
    new_total_price = price + total_price
    new_balance = balance - new_total_price
    if new_balance < 0 :
        print("not enough funds! You need an additional $", new_balance * -1)
    else :
        print("cart balance $", new_total_price)

def print_smallest(a:int, b:int, c:int) :
    """
    This function gets three integers a, b and c, and prints the smallest of the three
    >>> print_smallest(3, 5, -2)
    -2
    >>> print_smallest(3, 5, 3)
    3
    """
    if a > b :
        a += b
        b = a - b
        a -= b
    if a > c :
        a += c
        c = a - c
        a -= c
    print(a)

def is_multiple_of(n1:int, n2:int) :
    """
    This function get two integers n1 and n2, then determines whether n1 is a multiple of n2 or not.
    If it is, it will print n1 is a multiple of n2, and if it is not, it will print n1 is not a multiple of n2.
    >>> is_multiple_of(12, 3)
    12 is a multiple of 3
    >>> is_multiple_of(12, 5)
    12 is not a multiple of 5
    """
    if n1 % n2 == 0 :
        print(f"{n1} is a multiple of {n2}")
    else :
        print(f"{n1} is not a multiple of {n2}")

def print_triangle_type(a:int, b:int, c:int) :
    """
    This function gets three angles of a triangle and determines what kind of Triangle it is.
    If it is not a valid triangle, it prints invalid triangle
    If it is a right triangle, it prints right triangle
    If it is an obtuse triangle, it prints obtuse triangle
    If it is an acute triangle, it prints acute triangle
    >>> print_triangle_type(100, 50, 50)
    invalid triangle
    >>> print_triangle_type(90, 40, 50)
    right triangle
    >>> print_triangle_type(80, 60, 40)
    acute triangle
    >>> print_triangle_type(100, 30, 50)
    obtuse triangle
    """
    total_degree = a + b + c
    if total_degree > 180 :
        print("invalid triangle")
        return
    if a > 90 or b > 90 or c > 90 :
        print("obtuse triangle")
        return
    if a < 90 and b < 90 and c < 90 :
        print("acute triangle")
    if a == 90 or b == 90 or c == 90 :
        print("right triangle")

def print_time_in_seconds(days:int, hours:int, minutes:int, seconds:int) :
    """
    This funtion gets a time as 4 integers days, hours, minutes and seconds and converts this time to seconds.
    If any of the given numbers is negative, it prints invalid time, otherwise, it will print total time: X seconds, were X is
    the total time in seconds.
    >>> print_time_in_seconds(1, 1, 1, 1)
    total time: 90061 seconds
    >>> print_time_in_seconds(-1, 1, 1, 1)
    invalid time
    """
    if days < 0 or hours < 0 or minutes < 0 or seconds < 0 :
        print("invalid time")
        return
    total_time_in_seconds = seconds + minutes * 60 + hours * 60 * 60 + days * 24 * 60 * 60
    print(f"total time: {total_time_in_seconds} seconds")