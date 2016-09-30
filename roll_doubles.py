"""
Problem:

    A game involves rolling two dice and adding the scores together to
    calculate the number of points received. However, if a player rolls
    two dice with the same number, they receive double the points.

    The roll_double function takes in two numbers, one for each score
    on the dice. It should print out how many points the player should
    receive.

Tests:

    >>> roll_double(2, 5)
    7
    >>> roll_double(4, 5)
    9
    >>> roll_double(2, 2)
    8
    >>> roll_double(5, 5)
    20

"""

# Use this to test your solution. Don't edit it!
import doctest
def run_tests():
    doctest.testmod(verbose=True)


def roll_double(dice1, dice2):
    if dice1 == n and dice2 == i:
        print(n + i)

    elif dice1 == n and dice2 == i:
        print(n + i)

    elif dice1 == n and dice2 == n:
        print(n * n + n * n)

    elif dice1 == n and dice2 == n:
        print(n * n + n * n)
        
