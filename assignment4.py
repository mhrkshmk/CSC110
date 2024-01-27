import doctest

def is_proper_divisor(n1:int, n2:int) -> bool :
    """
    This function gets two integers n1 and n2 and return a boolean value, which is True if n1 is a proper divisor of n2, and False otherwise.
    >>> is_proper_divisor(1, 1)
    False
    >>> is_proper_divisor(0, 0)
    False
    >>> is_proper_divisor(3, 0)
    True
    >>> is_proper_divisor(0, 3)
    False
    >>> is_proper_divisor(2, 3)
    False
    >>> is_proper_divisor(2, 6)
    True
    """
    if n2 == 0 and n1 > 0:
        return True
    elif (n1 > 0 and n2 % n1 == 0 and n1 != n2) :
        return True
    else :
        return False
    
def sum_of_proper_divisors(n:int) -> int :
    """
    This funtion gets an integer n and return the sum of all of its proper_divisors
    >>> sum_of_proper_divisors(12)
    16
    >>> sum_of_proper_divisors(0)
    0
    >>> sum_of_proper_divisors(1)
    0
    """
    sum = 0
    for num in range(1, n) :
        sum += (is_proper_divisor(num, n) * num)
    return sum

def get_abundance(n:int) -> int :
    """
    This function gets an integer n and then returns the abundance of that number, but if the number is not an abundant number, it returns 0
    >>> get_abundance(12)
    4
    >>> get_abundance(0)
    0
    >>> get_abundance(1)
    0
    >>> get_abundance(9)
    0
    """
    sum = sum_of_proper_divisors(n)
    if sum <= n :
        return 0
    else :
        return sum - n
    
def get_multiples(begin:int, multiple:int, length:int) -> str :
    """
    This function return a string containing a sequence of multiples. It gets 3 integers begin, multiple, and length which determine the starting number of the 
    sequence, the number representing the multiple, and the number of values it should print.
    >>> get_multiples(8, 2, 7)
    '8 10 12 14 16 18 20'
    >>> get_multiples(9, 3, 6)
    '9 12 15 18 21 24'
    """
    multiple_sequence = ''
    next_num = begin
    count = 0
    while count < length :
        next_num = begin + multiple * count
        multiple_sequence += str(next_num)
        count += 1
        if count < length :
            multiple_sequence += ' '
    return multiple_sequence

def print_multiplication_table(horizontal:int, width:int, vertical:int, height:int) -> None :
    """
    This function will print a multiplication table, it will get 4 integers, the number to start the horizontal axis, the width of the table,
    the number to start the vertical axis at, and the height of the multiplication table, and then, it will print the multiplication table.
    >>> print_multiplication_table(0, 3, 4, 10)
     0 1 2
    4 0 4 8
    5 0 5 10
    6 0 6 12
    7 0 7 14
    8 0 8 16
    9 0 9 18
    10 0 10 20
    11 0 11 22
    12 0 12 24
    13 0 13 26
    """
    horizontal_axis = ' ' + get_multiples(horizontal, 1, width)
    print(horizontal_axis)
    for num in range(vertical, vertical + height) :
        sequence = str(num) + ' ' + get_multiples(vertical * horizontal, num, width)
        print(sequence)