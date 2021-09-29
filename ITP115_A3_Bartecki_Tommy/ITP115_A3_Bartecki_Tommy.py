# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 3
# Description:
# This program calculates the largest and smallest number entered by the user
# It also calculates the average of all entries

def main():
    repeat = "y"

    while repeat == "y" or repeat == "Y":
        # Reset all values for each set of numbers
        smallest = float('inf')
        largest = float('-inf')
        value = 0
        sum = 0.0
        count = 0.0
        print("Input an integer greater than or equal to 0 (-1 to quit)")
        while value != -1:
            value = int(input("> "))

            # Set smallest and largest values if not -1
            if value < smallest and value != -1:
                smallest = value
            if value > largest and value != -1:
                largest = value

            # Update totals
            if value != -1:
                sum += value
                count += 1

        # Calculate average if entries > 0
        if count != 0:
            average = sum / count
        else:
            average = 0

        print("The largest number is " + str(largest))
        print("The smallest number is " + str(smallest))
        print("The average number is " + str(average))

        # Restart the outer while loop if user wants to continue
        repeat = input("\nWould you like to enter another set of numbers? (y/n): ")

    print("\nGoodbye!")


main()
