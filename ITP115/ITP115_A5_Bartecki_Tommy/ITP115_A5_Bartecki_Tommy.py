# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 5
# Description:
# This program simulates a word scramble game
# It also takes in a string and encrypts it for the user

import random


def main():
    # List of possible words and associated hints
    words = ["cow", "pasta", "angel", "trojan", "concert", "lantern"]
    hints = ["Farm animal", "Italian food", "Flying creature", "USC", "Music", "Light"]

    # Select word randomly and get its index
    guessing_string = random.choice(words)
    index = words.index(guessing_string)
    count = 1
    guessing_list = list(guessing_string)
    jumbled = ""

    # Randomly go through each letter in word and add it to new string before deleting it
    while guessing_list:
        i = random.randint(0, len(guessing_list)-1)
        jumbled += guessing_list[i]
        del guessing_list[i]

    print("PART 1 - Word Jumble Game\n")
    print("The jumbled word is", jumbled)
    print("You will receive 5 points if you use a hint and 10 if not.")
    hint_given = False

    guess = input("Please enter your guess: ")

    # Continue prompting a guess until correct answer
    while guess != guessing_string:
        print("Try again.")
        # Only ask about hint if not already given
        if not hint_given:
            hint = input("Do you want a hint? (y/n) ")
            if hint == "y" or hint == "Y":
                print(hints[index])
                hint_given = True

        guess = input("Please enter your guess: ")
        count += 1

    # More points if hint is not used
    if hint_given:
        score = 5
    else:
        score = 10

    print("You got it!")
    print("It took you", str(count), "tries.")
    print("Your score is", str(score), "points\n")

    # Part 2 of Assignment
    print("\nPART 2 - Encrypt/Decrypt\n")
    message = input("Enter a message: ")
    shift = input("Enter a number to shift by (0-25): ")
    valid = False

    # Keep asking for shift value until proper input is received
    while not valid:
        while not shift.isdigit():
            shift = input("Enter a number to shift by (0-25): ")

        shift = int(shift)
        if 0 <= shift <= 25:
            valid = True
        else:
            shift = input("Enter a number to shift by (0-25): ")

    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    # Create cipher offset by the shift value entered
    cipher = alphabet[shift:] + alphabet[0:shift]

    print("Encrypting message....")
    encrypted = ""
    decrypted = ""

    # Go through each letter in the message and find the corresponding index in alphabet before matching w/ cipher
    for char in message:
        if char.isalpha():
            encrypted += cipher[alphabet.index(char)]
        else:
            encrypted += char

    print("\tEncrypted message:", encrypted)

    print("Decrypting message....")
    
    # Same process as encrypting but backwards
    for char in encrypted:
        if char.isalpha():
            decrypted += alphabet[cipher.index(char)]
        else:
            decrypted += char

    print("\tDecrypted message:", decrypted)
    print("\tOriginal message:", message)


main()
