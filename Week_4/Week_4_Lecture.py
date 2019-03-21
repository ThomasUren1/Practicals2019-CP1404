########################################################################################################################
#                           Part 1 - str.format()
########################################################################################################################

# name = input("Name: ")
# number_of_vowels = 0
# for characters in name.lower():
#     if characters in 'aeiou':
#         number_of_vowels += 1
#
# print("Out of {} letters, {} has {} vowels".format(len(name), name, number_of_vowels))


########################################################################################################################
#                           Part 2 - Enter scores then print highest
########################################################################################################################

# scores = []
# score = int(input("Score: "))
# while score >= 0:
#     # scores += [score] ## this is not used a lot of the method below is a better way to do it.
#     scores.append(score)
#     score = int(input("Score: "))
# print("Your highest score is", max(scores))

# this program will crash because there is no error checking if they user puts a negative number first

########################################################################################################################
#                           Part 3 - List Comprehension
########################################################################################################################


# text = "This is a sentence"
# long_words = [word for word in text.split() if len(word) > 3]
# print(long_words)

########################################################################################################################
#                           Part 3 - List Comprehension
########################################################################################################################

def print_olympic_years():
    years = range(1900, 2019, 4)
    print(years)
    return


print_olympic_years()

