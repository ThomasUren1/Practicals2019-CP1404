"""Prac 04 "Do-from-scratch" exercise"""

from random import randint

MAX_VALUE = 45
QUICK_PICKS_AMOUNT = 6


def main():
    number_of_picks = int(input("How many quick picks: "))
    for i in range(1, number_of_picks + 1):
        quick_picks = []
        # quick_string = ""
        for i in range(1, QUICK_PICKS_AMOUNT + 1):
            randomized_number = randint(1, MAX_VALUE)
            quick_picks.append(randomized_number)
            # quick_string += str(randomized_number)
            # quick_string += " "
        print("{:}".format(quick_picks))
        # print("{}".format(quick_string))


main()
