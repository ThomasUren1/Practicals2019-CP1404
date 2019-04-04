"""exercise in lists for Prac 04, CP1404"""
########################################################################################################################
#                           Part 1 - Basic list operations
########################################################################################################################


# This is the first part of the exercise
# def main():
#     numbers = []
#     SIZE_OF_LIST = 5
#     for i in range(1, SIZE_OF_LIST+1):
#         number = int(input("Number: "))
#         numbers.append(number)
#
#     average_number = sum(numbers)/len(numbers)
#     print("The first number is {}".format(numbers[0]))
#     print("The last number is {}".format(numbers[-1]))
#     print("The smallest number is {}".format(min(numbers)))
#     print("The largest number is {}".format(max(numbers)))
#     print("The average number is {}".format(average_number))
#
#
# main()


########################################################################################################################
#                           Part 2 - Woefully inadequate security checker
########################################################################################################################


usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    username = input("Enter your username: ")
    if username in usernames:
        print("Access Granted!")
    else:
        print("Access Denied!")


main()
