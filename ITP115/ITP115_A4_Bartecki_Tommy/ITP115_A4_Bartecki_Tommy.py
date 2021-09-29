# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 4
# Description:
# This program counts the instances of each character in a word and displays it
# It also simulates a dice game

import random


def main():
    print("PART 1 - Character Counter")
    sentence = input("Please enter a sentence: ")

    # Initialize count list for each letter and special characters
    counts = ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
              "", ""]

    # Go through each letter in sentence and increase instances for each
    for letter in sentence:
        if letter == "a" or letter == "A":
            counts[1] += "*"
        elif letter == "b" or letter == "B":
            counts[2] += "*"
        elif letter == "c" or letter == "C":
            counts[3] += "*"
        elif letter == "d" or letter == "D":
            counts[4] += "*"
        elif letter == "e" or letter == "E":
            counts[5] += "*"
        elif letter == "f" or letter == "F":
            counts[6] += "*"
        elif letter == "g" or letter == "G":
            counts[7] += "*"
        elif letter == "h" or letter == "H":
            counts[8] += "*"
        elif letter == "i" or letter == "I":
            counts[9] += "*"
        elif letter == "j" or letter == "J":
            counts[10] += "*"
        elif letter == "k" or letter == "K":
            counts[11] += "*"
        elif letter == "l" or letter == "L":
            counts[12] += "*"
        elif letter == "m" or letter == "M":
            counts[13] += "*"
        elif letter == "n" or letter == "N":
            counts[14] += "*"
        elif letter == "o" or letter == "O":
            counts[15] += "*"
        elif letter == "p" or letter == "P":
            counts[16] += "*"
        elif letter == "q" or letter == "Q":
            counts[17] += "*"
        elif letter == "r" or letter == "R":
            counts[18] += "*"
        elif letter == "s" or letter == "S":
            counts[19] += "*"
        elif letter == "t" or letter == "T":
            counts[20] += "*"
        elif letter == "u" or letter == "U":
            counts[21] += "*"
        elif letter == "v" or letter == "V":
            counts[22] += "*"
        elif letter == "w" or letter == "W":
            counts[23] += "*"
        elif letter == "x" or letter == "X":
            counts[24] += "*"
        elif letter == "y" or letter == "Y":
            counts[25] += "*"
        elif letter == "z" or letter == "Z":
            counts[26] += "*"
        elif letter == " ":
            counts[27] += "*"
        else:
            counts[0] += "*"

    print("\nHere is the character distribution:\n")

    print("special characters:", counts[0])
    # Use ASCII values to output letter along with count from count list
    for i in range(1, 27):
        if counts[i] != "":
            print(chr(i + 96) + ": " + counts[i])
        else:
            print(chr(i + 96) + ": NONE")

    print("\nPART 2 - D20 Dice Game\n")
    score = 0
    # Repeat 10 times
    for i in range(10):
        case = random.randrange(1, 6)
        print("You are playing for CASE", case)
        print("You will win for the following numbers:")
        roll = random.randrange(1, 21)
        win = False

        # Win with even numbers
        if case == 1:
            for j in range(2, 21, 2):
                print(j, end="  ")
                if roll % 2 == 0:
                    win = True
        # With with odd numbers
        elif case == 2:
            for j in range(1, 20, 2):
                print(j, end="  ")
                if roll % 2 == 1:
                    win = True
        # Win with numbers 5-10 inclusive
        elif case == 3:
            for j in range(5, 11):
                print(j, end="  ")
                if 4 < roll < 11:
                    win = True
        # Win with even numbers greater than 10
        elif case == 4:
            for j in range(10, 21, 2):
                print(j, end="  ")
                if roll >= 10 and roll % 2 == 0:
                    win = True
        # Win with multiples of 3
        elif case == 5:
            for j in range(3, 21, 3):
                print(j, end="  ")
                if roll % 3 == 0:
                    win = True

        print("\n\nNow rolling... \nYou rolled a " + str(roll) + "!")
        # If win variable is true, add to total score then repeat until 10th game
        if win:
            print("You won 50 points! :)\n")
            score += 50
        else:
            print("You didn't win :( \n")

    print("Your total score is: " + str(score))
    print("Thanks for playing!")


main()
