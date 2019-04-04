"""Week 2 Practical for CP1404"""

########################################################################################################################
#                           Part 1 - using the format function
########################################################################################################################

# user_name = "Tom"
# user_age = 25
#
# print("{:>10} is {} years old".format(user_name, user_age))

########################################################################################################################
#                           Part 2 - using random numbers
########################################################################################################################

# import random
# print(random.randint(5, 20))  # line 1
# print(random.randrange(3, 10, 2))  # line 2
# print(random.uniform(2.5, 5.5))  # line 3

########################################################################################################################
#                           Part 3 - fill in the blanks
########################################################################################################################

# finished = False
# result = 0
# while not finished:
#     try:
#         result = int(input("Enter a number: "))
#         finished = True
#         pass
#     except ValueError:
#         print("Please enter a valid integer.")
#
# print("Valid result is:", result)


########################################################################################################################
#                           Part 4 - file opener
########################################################################################################################

# a

########################################################################################################################
#                           Part 5 - password checker
########################################################################################################################

"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    from string import ascii_lowercase
    from string import ascii_uppercase
    from string import digits

    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char in ascii_lowercase:
            count_lower += 1
        elif char in ascii_uppercase:
            count_upper += 1
        elif char in digits:
            count_digit += 1
        # TODO: count each kind of character (use str methods like isdigit)
        pass

    # TODO: if any of the 'normal' counts are zero, return False
    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False

    # TODO: if special characters are required, then check the count of those
    # and return False if it's zero

    if SPECIAL_CHARS_REQUIRED:
        for char in password:
            if char in SPECIAL_CHARACTERS:
                count_special += 1
        if count_special == 0:
            return False

    # if we get here (without returning False), then the password must be valid
    return True


main()
