# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 2
# Description:
# This program creates a Harry Potter vending machine.
# It determines change and gives a discount.

def main():
    # Receiving user choice of item
    choice = input("Please select an item from the vending machine: \n\t"
                   "  a) Butterbeer: 58 knuts \n\t  b) Quill: 10 knuts \n\t"
                   "  c) The Daily Prophet: 7 knuts\n\t  d) Book of Spells: 400 knuts\n\t"
                   "  e) Wand: 635 knuts \n> ")

    # Check if invalid option and assign butterbeer before moving on
    if (choice != "a" and choice != "A" and choice != "b" and choice != "B" and
            choice != "c" and choice != "C" and choice != "d" and choice != "D" and choice != "e" and choice != "E"):
        print("You have entered an invalid option. You will be given a Butterbeer for 58 knuts.")
        choice = "a"

    insta = input("Will you share this on Instagram? (y/n): ")
    # Initializing values for change
    coupon = 0
    cost = 0

    # If they will share, increase coupon to 5
    if insta == "y" or insta == "Y":
        print("Thanks! You get 5 knuts off your purchase \n")
        coupon = 5
    elif insta == "n" or insta == "N":
        print("")
    else:
        print("You have entered an invalid option. No coupon will be used \n")

    # For extra credit-> Can pay with any mix of coins
    galleons = input("How many galleons would you like to pay with? ")
    sickles = input("How many sickles would you like to pay with? ")
    knuts = input("How many knuts would you like to pay with? ")
    print()

    # If non-numeric entry, set amount to 0
    if not galleons.isnumeric():
        print("Invalid galleon entry. Galleons set to 0.")
        galleons = 0
    if not sickles.isnumeric():
        print("Invalid sickles entry. Sickles set to 0.")
        sickles = 0
    if not knuts.isnumeric():
        print("Invalid knuts entry. Knuts set to 0.")
        knuts = 0

    print()
    galleons = int(galleons)
    sickles = int(sickles)
    knuts = int(knuts)

    # Calculate total paid with in knuts
    change = galleons * 493 + sickles * 29 + knuts

    # Based on input, output correct response and update total cost
    if (choice == "a" or choice == "A") and change >= (58 - coupon):
        print("You bought a Butterbeer for 58 knuts (with coupon of", coupon, "knuts) and "
                "paid with " + str(galleons) + " galleons, " + str(sickles) + " sickles, and " + str(knuts) + " knuts.")
        cost = 58 - coupon
    elif (choice == "b" or choice == "B") and change >= (10 - coupon):
        print("You bought a Quill for 10 knuts (with coupon of", coupon, "knuts) and"
                " paid with " + str(galleons) + " galleons, " + str(sickles) + " sickles, and " + str(knuts) + " knuts.")
        cost = 10 - coupon
    elif (choice == "c" or choice == "C") and change >= (7 - coupon):
        print("You bought a Daily Prophet for 7 knuts (with coupon of", coupon, "knuts) and"
                " paid with " + str(galleons) + " galleons, " + str(sickles) + " sickles, and " + str(knuts) + " knuts.")
        cost = 7 - coupon
    elif (choice == "d" or choice == "D") and change >= (400 - coupon):
        print("You bought a Book of Spells for 400 knuts (with coupon of", coupon, "knuts) and"
                " paid with " + str(galleons) + " galleons, " + str(sickles) + " sickles, and " + str(knuts) + " knuts.")
        cost = 400 - coupon
    elif (choice == "e" or choice == "E") and change >= (635 - coupon):
        print("You bought a Wand for 635 knuts (with coupon of", coupon, "knuts) and"
                " paid with " + str(galleons) + " galleons, " + str(sickles) + " sickles, and " + str(knuts) + " knuts.")
        cost = 635 - coupon
    # If not enough money, terminate program
    else:
        print("Sorry, you do not have enough money.")
        exit()

    # Calculations for correct change
    change -= cost
    temp_change = change
    end_galleons = int(change / 493)
    change -= (end_galleons*493)
    end_sickles = int(change / 29)
    end_knuts = change % 29

    print("\nHere is your change (" + str(temp_change) + " knuts): \nGalleons: " + str(end_galleons) + "\nSickles: "
          + str(end_sickles) + "\nKnuts: " + str(end_knuts))


main()
