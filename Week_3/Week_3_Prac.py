########################################################################################################################
#                           Part 1 - password checking. incomplete.
########################################################################################################################
# """This program checks a users password to ensure it meets a standard. One upper case. One lower case. One number."""
#
# from string import ascii_lowercase
#
#
# def is_valid_password(string):
#     count = 0
#     for character in string.lower():
#         if character in ascii_lowercase:
#             count += 1
#     return count
#
#
# def is_valid_password_hidden(string):
#     user_password_hidden = string
#     for character in string:
#         user_password_hidden[character] = "*"
#     return user_password_hidden
#
# user_password = "Hello world"
#
# if is_valid_password(user_password) < 6:
#     print("password is not long enough! >:(")
# else:
#     user_password_hidden = user_password
#     print(is_valid_password_hidden(user_password))

########################################################################################################################
#                           Part 2 - directory peeking ;D
########################################################################################################################

# import os
#
# print("The files and folders in {} are:".format(os.getcwd()))
# items = os.listdir('.')
# for item in items:
#     print(item)

########################################################################################################################
#                           Part 3 - extension work, temperature converting (incomplete)
########################################################################################################################


# def celsius_to_fahrenheit(temperature):
#     fahrenheit_temperature = temperature*1.8 + 32
#     return fahrenheit_temperature
#
#
# def FahrenheitToCelsius(temperature):
#     celsius_temperature = (temperature-32)/1.8
#     return celsius_temperature
#
# temperature = int(input("Enter the temperature to convert: "))
#
# print("The temperature is: {}".format(celsius_to_fahrenheit(temperature)))

