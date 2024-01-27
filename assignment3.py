import doctest

def get_smallest(a:int, b:int, c:int) -> int:
    """
    This function gets three integers a, b, and c, and prints the smallest of the three
    >>> get_smallest(3, 5, -2)
    -2
    >>> get_smallest(3, 5, 3)
    3
    """
    if a > b:
        a += b
        b = a - b
        a -= b
    if a > c:
        a += c
        c = a - c
        a -= c
    return a

def get_time_in_seconds(days:int, hours:int, minutes:int, seconds:int) -> int:
    """
    This function gets the time as 4 integer days, hours, minutes, seconds and converts this time to seconds.
    >>> get_time_in_seconds(1, 1, 1, 1)
    90061
    """
    total_time_in_seconds = days * 24 * 60 * 60 + hours * 60 * 60 + minutes * 60 + seconds
    return total_time_in_seconds

def get_average_speed(kilometers:float, days:int, hours:int, minutes:int, seconds:int) -> float:
    """
    This function get the distance traveled in kilometers as float and the number of days, hours, minutes and seconds traveled as integers,
    and will return the average speed of the vehicle in meters per second.
    >>> get_average_speed(170863.9, 1, 1, 1, 1)
    1897.2018964923775
    """
    meters = kilometers * 1000
    total_time_in_seconds = get_time_in_seconds(days, hours, minutes, seconds)
    average_speed = meters / total_time_in_seconds
    return average_speed

def get_box_charge(quantity:int, price:float) -> float:
    """
    This function gets the number of boxes of contact lenses bought as integer, and the price of each box.
    However, if there are 10 or more boxes bought, a 10% discount will be given, and if 20 or more boxes are bought, a 20% discount will be given.
    >>> get_box_charge(5, 12.5)
    62.5
    >>> get_box_charge(15, 12.5)
    168.75
    >>> get_box_charge(25, 12.5)
    250.0
    """
    total_price = quantity * price
    if quantity >= 10 and quantity < 20 :
        total_price *= 90 / 100
    elif quantity >= 20 :
        total_price *= 80 / 100
    return total_price

def get_order_charge(new:bool, prescription1:int, price1:float, prescription2:int, price2:float) -> float:
    """
    This function gets 2 type of prescribed contact lenses as integers, their prices as float, and a boolean to determine if the customer is new or not.
    it will calculate the total price to be paid for the prescriptions, and will add a 10% discount if the customer is new, then it will get the 7% pst charge of total price and the 5% gst charge of total price, 
    then if the order is more than $0 and less than $100, it will add a $4.50 shipping charge.
    >>> get_order_charge(False, 1, 12.5, 2, 9.5)
    39.78
    >>> get_order_charge(True, 11, 12.5, 5, 9.5)
    172.62
    """
    total_price_prescription1 = get_box_charge(prescription1, price1)
    total_price_prescription2 = get_box_charge(prescription2, price2)
    total_price = total_price_prescription1 + total_price_prescription2
    new_customer_discount = total_price * new * 10 / 100
    total_price -= new_customer_discount
    pst_charge = total_price * 7 / 100
    gst_charge = total_price * 5 / 100
    total_price += pst_charge + gst_charge
    shipping_charge = (total_price > 0) * (total_price < 100) * 4.50
    total_price += shipping_charge
    return total_price

def place_order(balance:float, new:bool, prescription1:int, price1:float, prescription2:int, price2:float) -> bool:
    """
    This function gets the balance of a customer as float, whether they are new or not as a bool, number of prescription1 wanted as integers, price of each box of prescription1 as float, number of prescription2 wanted 
    as integers, and the price of each box of prescription2 as float. then by using get_order_charge function it will calculate the total price the customer has to pay, and if their balance is at least that much it will
    return True, otherwise it will return False.
    >>> place_order(40.50, False, 1, 12.50, 2, 9.5)
    True
    >>> place_order(32.75, False, 1, 12.50, 2, 9.5)
    False
    """
    total_price = get_order_charge(new, prescription1, price1, prescription2, price2)
    return total_price <= balance

def get_middle(s:str) -> str:
    """
    This function gets an string and returns the middle character(s) of that string, if its length is odd, it will return the single middle one, and if its even, it will return the two middle characters.
    >>> get_middle('Victoria')
    'to'
    >>> get_middle('Vancouver')
    'o'
    >>> get_middle('')
    ''
    """
    n = len(s)
    if n == 0 :
        return s
    if len(s) % 2 == 1 :
        return s[n // 2]
    else :
        t = s[n // 2 - 1] + s[n // 2]
        return t