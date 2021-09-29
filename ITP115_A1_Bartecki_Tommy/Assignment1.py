# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 1
# Description:
# This program creates a Mad Libs story.
# It gets input from the user and prints output.

def main():
    # getting user input in correct format
    animal = input("Enter an animal (plural): ")
    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter another adjective: ")
    verb = input("Enter a verb: ")
    ing_verb = input("Enter a verb ending in \'ing\': ")
    num_one = int(input("Enter a number: "))
    num_two = int(input("Enter a second number: "))
    num_three = int(input("Enter a third number: "))
    dec_num = float(input("Enter a number with a decimal: "))

    # Printing Mad Libs with correct spacing and user input in quotes
    print("Today I adopted \"" + str(num_one) + "\" pet \"" + animal + "\". I learned that each animal needs \"" +
          str(dec_num) + "\" hours of \"" + ing_verb + "\" every day, and that they travel in groups of \"" +
          str(num_two) + "\". They are so \"" + adjective1 + "\" that I decided to adopt \"" + str(num_three) +
          "\" more. Now I have \"" + str(num_one + num_three) + "\" \"" + animal + "\" and I am so \"" + adjective2 +
          "\" that I want to \"" + verb + "\".")


main()
