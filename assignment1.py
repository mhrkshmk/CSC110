def print_wolf() :
    """
    This function prints a wolf ascii art design
    The credit for this design goes to https://www.asciiart.eu/animals
    Art by Morfina
    """
    print("                        ,     ,")
    print("                        |\---/|")
    print("                       /  , , |")
    print("                  __.-'|  / \ /")
    print("         __ ___.-'        ._O|")
    print("      .-'  '        :      _/")
    print("     / ,    .   \"    .     |")
    print("    :  ;    :        :   _/")
    print("    |  |   .'     __:   /")
    print("    |  :   /'----'| \  |")
    print("    \  |\  |      | /| |")
    print("     '.'| /       || \ |")
    print("     | /|.'       '.l \\_")
    print("snd  || ||             '-'")
    print("     '-''-'")

def print_deer() :
    """
    This function prints a deer in ascii art design
    The credit for this design goes to https://www.asciiart.eu/animals/deer
    Art by philip Powell
    """
    print(" ,_)/")
    print("  (-'")
    print(" .-'\ ")
    print("  \"\'\'\"\"\"\"\"\'),")
    print("     )/---,( ")
    print("PjP / \  / |      , '     , '   , '   ,'   ,'    ,'   ;     ;")

def print_logo() :
    print("/~~~~~~~~\\")
    print_wolf()
    print("/~~~~~~~~\\")
    print_deer()
    print("/~~~~~~~~\\")
    print_wolf()
    print("/~~~~~~~~\\")
    print_deer()
    print("/~~~~~~~~\\")

def calculate_surface_area(height:float, diameter:float) :
    """
    This function gets the height and the diameter of a cylinder as float numbers,
    and first calculates the area of top of the cylinder and the walls of the cylinder and stores them in variables,
    and since the area of the bottom of the cylinder is equal to area of the top of cylinder,
    it adds the area of top of the cylinder multiplied by 2, to the area of walls and prints the results.
    >>> calculate_surface_area(19.7, 2.22)
        cylinder area: 145.1
    """
    PI = 3.14
    radius = diameter / 2
    surface_of_top = PI * radius * radius
    surface_of_walls = 2 * PI * radius * height
    surface_of_cylinder = surface_of_top * 2 + surface_of_walls;
    print("cylinder area:", "{0:.1f}".format(surface_of_cylinder))