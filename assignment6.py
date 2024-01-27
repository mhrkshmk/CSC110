import doctest

def multiply_by(numbers: list[int], multiplier:int) -> list[int] :
    """
    This function gets a list of integers and an integer named multiplier, then it will return a new function with every element in the old function multiplied by 
    the multiplier.
    >>> multiply_by([1, 2, 3, 4, -5], 2)
    [2, 4, 6, 8, -10]
    >>> multiply_by([1, 2, 3, 4, 5], -2)
    [-2, -4, -6, -8, -10]
    >>> multiply_by([], 10)
    []
    """
    new_list = []
    for index in range(len(numbers)) :
        new_list.append(numbers[index] * multiplier)
    return new_list

def is_multiple_of(n1:int, n2:int) -> bool :
    """
    This function get two integers n1 and n2, then determines whether n1 is a multiple of n2 or not.
    If it is, it will print n1 is a multiple of n2, and if it is not, it will print n1 is not a multiple of n2.
    >>> is_multiple_of(12, 3)
    True
    >>> is_multiple_of(12, 5)
    False
    >>> is_multiple_of(12, 0)
    False
    >>> is_multiple_of(0, 12)
    True
    >>> is_multiple_of(0, 0)
    True
    >>> is_multiple_of(12, -3)
    True
    >>> is_multiple_of(-12, 5)
    False
    >>> is_multiple_of(-12, -3)
    True
    """
    if n1 == 0 :
        return True
    else :
        if n2 == 0 :
            return False
        elif n1 % n2 == 0 :
            return True
        else :
            return False
        
def remove_multiples(numbers: list[int], n:int) -> list[int] :
    """
    This Function is a helper function.
    This function gets a list of integers and an integer named n, it will then create and return a new list consisting of only the elements in the original set that
    are not a multiple of n.
    >>> remove_multiples([1,2,3,4,5,6,7,8,9,10], 2)
    [1, 3, 5, 7, 9]
    >>> remove_multiples([1,2,3,4,5,-6,-7,-8,9,-10], 2)
    [1, 3, 5, -7, 9]
    >>> remove_multiples([1,2,3,4,5,6,7,8,9,10], -2)
    [1, 3, 5, 7, 9]
    >>> remove_multiples([], 3)
    []
    """
    new_list = []
    for index in range(len(numbers)) :
        is_multiple = is_multiple_of(numbers[index], n)
        if not(is_multiple) :
            new_list.append(numbers[index])
    return new_list

def are_ends_similar(str1: str, str2: str) -> bool :
    """
    This function is a helpert function.
    This function gets 2 string str1 and str2 and return a boolean value which is True if str1 ends with str2 and False otherwise.
    >>> are_ends_similar('ABcD', 'cD')
    True
    >>> are_ends_similar('ABcD', 'CD')
    True
    >>> are_ends_similar('', 'cD')
    False
    >>> are_ends_similar('ABcD', '')
    True
    """
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str2) > len(str1) :
        return False
    else :
        if str1[(len(str1) - len(str2)):] == str2 :
            return True
        else :
            return False

def remove_ends_with(str_list: list[str], str1:str) -> list[str] :
    """
    This function gets a list of strings and a string named str1, it will then create and return a new list which contains every element of the first list, except
    the ones ending with str1.
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'], 'at')
    ['ratchet', 'atlas']
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'], 'AT')
    ['ratchet', 'atlas']
    >>> remove_ends_with(['bat', 'ratchet', 'BCAT', 'at', 'atlas'], '')
    []
    >>> remove_ends_with([], 'AT')
    []
    """
    new_list = []
    for index in range(len(str_list)) :
        if not(are_ends_similar(str_list[index], str1)) :
            new_list.append(str_list[index])
    return new_list

def get_index_of_largest(numbers: list[int]) -> int :
    """
    This function gets a list of integers and returns the index of the largest value in the list. and if there are more than one such values, it will return
    the index of the last occurrence.
    >>> get_index_of_largest([1,2,3,4,5])
    4
    >>> get_index_of_largest([1,2,2,2,4,2,4])
    6
    >>> get_index_of_largest([1,2,3,4,5,-1,5])
    6
    >>> get_index_of_largest([-1,-2,-3,-1])
    3
    """
    maximum_index = -1
    maximum = -1
    for index in range(len(numbers)) :
        if numbers[index] >= maximum :
            maximum_index = index
            maximum = numbers[index]
    return maximum_index

def is_proper_divisor(n1:int, n2:int) -> bool :
    """
    This function is a helper function.
    This function gets two integers n1 and n2 and return a boolean value, which is True if n1 is a proper divisor of n2, and False otherwise.
    >>> is_proper_divisor(1, 1)
    True
    >>> is_proper_divisor(0, 0)
    True
    >>> is_proper_divisor(3, 0)
    True
    >>> is_proper_divisor(0, 3)
    False
    >>> is_proper_divisor(2, 3)
    False
    >>> is_proper_divisor(2, 6)
    True
    """
    if n2 == 0 :
        return True
    elif (n1 > 0 and n2 % n1 == 0) :
        return True
    else :
        return False
    
def does_contain_proper_divisor(numbers: list[int], n:int) -> bool :
    """
    This function gets a list of integers and an integer n, and return True if any of the numbers in the list are a proper divisor of n, and will return False 
    otherwise.
    >>> does_contain_proper_divisor([3, 3, 4, 5], 4)
    True
    >>> does_contain_proper_divisor([3, 3, 4, 5], 0)
    False
    >>> does_contain_proper_divisor([3, 3, 4, 0], 0)
    True
    >>> does_contain_proper_divisor([3, 3, 0, 5], -4)
    True
    >>> does_contain_proper_divisor([], 4)
    False
    """
    for index in range(len(numbers)) :
        if is_proper_divisor(n, numbers[index]) :
            return True
    return False

def are_all_less_than_threshold(numbers: list[int], threshold: int) -> bool :
    """
    This function gets a list of integers and in integer threshold, and will return True if all values in the function are less than the given threshold, and will
    return False otherwise.
    >>> are_all_less_than_threshold([1,2,3,4,5], 5)
    False
    >>> are_all_less_than_threshold([1,2,3,4,5], -5)
    False
    >>> are_all_less_than_threshold([1,2,3,4,5], 6)
    True
    >>> are_all_less_than_threshold([1,2,3,4,-5], 5)
    True
    >>> are_all_less_than_threshold([], 0)
    True
    """
    for index in range(len(numbers)) :
        if numbers[index] >= threshold :
            return False
    return True