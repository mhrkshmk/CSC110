import doctest
import random

MIN_DIE = 1
MAX_DIE = 6

def roll_one_die() -> int:
    """ 
    simulates the roll of a single dice between MIN_DIE and MAX_DIE inclusive 
    and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    #generates a random number between MIN_DIE and MAX_DIE inclusive
    die = random.randint(MIN_DIE, MAX_DIE)
    
    #for testing to allow you to enter the dice roll you want at the keyboard
    #comment out the line above and uncomment this line:
    #die = int(input('enter a simulated dice roll\n'))
    
    return die

def get_sum_of_digits(num:int) -> int :
    """
    This function takes in an integer and return its sum of digits
    >>> get_sum_of_digits(0)
    0
    >>> get_sum_of_digits(432)
    9
    >>> get_sum_of_digits(-571)
    13
    """
    sum = 0
    if num < 0 :
        num *= -1
    while num > 0 :
        remainder = num % 10
        num //= 10
        sum += remainder
        
    return sum

def is_harshad_number(num:int) -> bool :
    """
    This function gets an integer and return a boolean which indicates if that number is a harshad number or not
    >>> is_harshad_number(432)
    True
    >>> is_harshad_number(433)
    False
    """
    sum = get_sum_of_digits(num)
    return (num % sum == 0)

def get_first_n_harshad_numbers(n:int) -> str :
    """
    This function gets an integer n and prints the first n harshad numbers
    >>> get_first_n_harshad_numbers(0)
    ''
    >>> get_first_n_harshad_numbers(1)
    '1'
    >>> get_first_n_harshad_numbers(20)
    '1,2,3,4,5,6,7,8,9,10,12,18,20,21,24,27,30,36,40,42'
    """
    num = 1
    count = 0
    harshad_sequence = ''
    while count < n:
        is_harshad = is_harshad_number(num)
        if is_harshad == True :
            harshad_sequence += str(num)
            count += 1
            if count < n :
                harshad_sequence += ',';
        num += 1
    return harshad_sequence

def play(guess1:int, guess2:int, bet:int) -> None :
    """
    This funtion gets three integers guess1, guess2 and bet. the first two are the players guess of two dice rolls, and the third is the amount of money they want to
    bet. then it will randomly roll a dice and if both guesses are correct, it will print that the player has won 3 times more money than they bet, if one of the guesses is right, it will keep rolling dices until the other guess is reached, but if the sum of rolls are equal to the sum of the first roll, then the player will lose, no matter what, but if the guess is reached before the losing target sum is reached, the player's money will double. And if both of the guesses are wrong, all the player's money is lost.
    """
    print(f"You guessed {guess1} and {guess2} will be rolled and bet ${bet} on the game")
    die1 = roll_one_die()
    die2 = roll_one_die()
    print(f"You rolled {die1} and {die2}")
    losing_target = die1 + die2
    if (die1 == guess1 and die2 == guess2) or (die1 == guess2 and die2 == guess1) :
        print("You guessed both correctly!")
        print(f"You now have ${bet * 3}")
    elif die1 == guess1 or die2 == guess1:
        print(f"You guessed {guess1} correctly, so you get another chance until you roll {guess2}, but if your sum equales {losing_target}, you lose")
        valid = True
        while valid == True :
            second_die1 = roll_one_die()
            second_die2 = roll_one_die()
            print(f"You rolled {second_die1} and {second_die2}")
            sum = second_die1 + second_die2
            if sum == losing_target :
                print(f"Sorry, your sum equales the losing target, you lose!")
                print("You now have $0")
                valid = False
            elif second_die1 == guess2 or second_die2 == guess2 :
                print(f"You rolled {guess2}, you win!")
                print(f"You now have ${bet * 2}")
                valid = False
    elif die1 == guess2 or die2 == guess2:
        print(f"You guessed {guess2} correctly, so you get another chance until you roll {guess1}, but if your sum equales {losing_target}, you lose")
        valid = True
        while valid == True :
            second_die1 = roll_one_die()
            second_die2 = roll_one_die()
            print(f"You rolled {second_die1} and {second_die2}")
            sum = second_die1 + second_die2
            if sum == losing_target :
                print(f"Sorry, your sum equales the losing target, you lose!")
                print("You now have $0")
                valid = False
            elif second_die1 == guess1 or second_die2 == guess1 :
                print(f"You rolled {guess1}, you win!")
                print(f"You now have ${bet * 2}")
                valid = False
    elif die1 != guess1 and die2 != guess2 :
        print("You guessed both numbers wrong. You lose!")
        print("You now have $0")