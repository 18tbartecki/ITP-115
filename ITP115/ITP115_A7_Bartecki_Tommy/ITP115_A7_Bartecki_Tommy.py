# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 7
# Description:
# This program let's users play Rock, Paper, Scissors against a computer

import random


# Displays starting menu to users
def displayMenu():
    print("\nWelcome! Let's play rock, paper, scissors. \nThe rules of the game are:")
    print("\tRock smashes scissors \n\tScissors cut paper \n\tPaper covers rock")
    print("\tIf both the choices are the same, it's a tie")


# Simulates the computer picking their move
def getComputerChoice():
    return random.randrange(0, 3)


# Asks user for their choice until proper input
def getPlayerChoice():
    user_choice = input("Please choose (0) for rock, (1) for paper or (2) for scissors\n")

    while user_choice != "0" and user_choice != "1" and user_choice != "2":
        user_choice = input("Invalid option.\nPlease choose (0) for rock, (1) for paper or (2) for scissors\n")

    return user_choice


# Simulates a round of the game and returns who wins
# -1 for computer win, 0 for tie, 1 for player win
def playRound(computerChoice, playerChoice):
    if playerChoice == 0:
        print("You chose Rock.")
        if computerChoice == 0:
            return 0
        elif computerChoice == 1:
            return -1
        else:
            return 1
    elif playerChoice == 1:
        print("You chose Paper")
        if computerChoice == 0:
            return 1
        elif computerChoice == 1:
            return 0
        else:
            return -1
    else:
        print("You chose Scissors.")
        if computerChoice == 0:
            return -1
        elif computerChoice == 1:
            return 1
        else:
            return 0


# Asks user if they want to continue and returns true or false
def continueGame():
    again = ""

    while again != "y" and again != "Y" and again != "n" and again != "N":
        again = input("Do you want to continue playing (y or n)? ")

    if again == "y" or again == "Y":
        return True
    else:
        return False


def main():
    # Variables to track game outcomes
    wins = 0
    losses = 0
    ties = 0
    continue_game = True

    while continue_game:
        displayMenu()
        computer_choice = getComputerChoice()
        user_choice = getPlayerChoice()
        user_choice = int(user_choice)

        outcome = playRound(computer_choice, user_choice)
        # Computer won -- display appropriate response and update loss counter
        if outcome == -1:
            losses += 1
            if user_choice == 0:
                print("The computer chose Paper.")
                print("Paper covers Rock. Computer wins!")
            elif user_choice == 1:
                print("The computer chose Scissors.")
                print("Scissors cut paper. Computer wins!")
            else:
                print("The computer chose Rock.")
                print("Rock smashes scissors. Computer wins!")
        # Tie with computer
        elif outcome == 0:
            ties += 1
            if user_choice == 0:
                print("The computer chose Rock.")
                print("You tied!")
            elif user_choice == 1:
                print("The computer chose Paper.")
                print("You tied!")
            else:
                print("The computer chose Scissors.")
                print("You tied!")
        # Win for the player
        else:
            wins += 1
            if user_choice == 0:
                print("The computer chose Scissors.")
                print("Rock smashes Scissors. You win!")
            elif user_choice == 1:
                print("The computer chose Rock.")
                print("Paper covers Rock. You win!")
            else:
                print("The computer chose Paper.")
                print("Scissors cut Paper. You win!")

        continue_game = continueGame()

    # Outputs number of all the results
    print("\nYou won " + str(wins) + " game(s).\n"
          "The computer won " + str(losses) + " game(s).\n"
          "You tied with the computer " + str(ties) + " time(s).\n")

    print("Thanks for playing!")


main()
