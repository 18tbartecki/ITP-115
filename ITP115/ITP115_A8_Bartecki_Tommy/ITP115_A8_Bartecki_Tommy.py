# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 8
# Description:
# This program simulates a game of Tic Tac Toe

import TicTacToeHelper


# Print the board nicely divided by lines
def printPrettyBoard(boardList):
    print()
    counter = 0
    for i in range(3):
        for j in range(3):
            if j != 2:
                print(boardList[counter], end=" | ")
            else:
                print(boardList[counter])
            counter += 1
        print("---------", end="")
        print()


# Checks if number is a digit then within the bounds of the board and not occupied
def isValidMove(boardList, spot):
    valid = True

    if not spot.isdigit():
        valid = False
    elif int(spot) > 8 or int(spot) < 0:
        valid = False
    elif boardList[int(spot)] == "x" or boardList[int(spot)] == "o":
        valid = False
    return valid


# Updates game board with next move
def updateBoard(boardList, spot, playerLetter):
    boardList[int(spot)] = playerLetter


def playGame():
    board = list(range(9))
    turns = 0
    gameOver = False

    # While no one has won continue
    while not gameOver:
        printPrettyBoard(board)
        # Whether x or o's turn
        if turns % 2 == 0:
            choice = input("Player x, pick a spot: ")
            validMove = isValidMove(board, choice)
            # Ensures board is updated with valid choice
            while not validMove:
                print("Invalid move, please try again.")
                choice = input("Player x, pick a spot: ")
                validMove = isValidMove(board, choice)

            updateBoard(board, choice, "x")
        else:
            choice = input("Player o, pick a spot: ")
            validMove = isValidMove(board, choice)
            while not validMove:
                print("Invalid move, please try again.")
                choice = input("Player o, pick a spot: ")
                validMove = isValidMove(board, choice)

            updateBoard(board, choice, "o")

        turns += 1
        # Checks if the game has a winner yet and responds appropriately
        winner = TicTacToeHelper.checkForWinner(board, turns)
        if winner == "x":
            gameOver = True
            printPrettyBoard(board)
            print("\nGame Over!\nPlayer x is the winner!")
        elif winner == "o":
            gameOver = True
            printPrettyBoard(board)
            print("\nGame Over!\nPlayer o is the winner!")
        elif winner == "s":
            gameOver = True
            printPrettyBoard(board)
            print("\nGame Over!\nStalemate reached!")


def main():
    print("Welcome to Tic Tac Toe!")
    another = "y"
    # Continues as long as the user wants to
    while another == "y" or another == "Y":
        playGame()
        another = input("Would you like to play another round? (y/n): ")

    print("Goodbye!")


main()
