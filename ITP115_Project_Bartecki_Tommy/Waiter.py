# This file defines the Waiter class
# This class will represent the restaurant’s waiter. The waiter maintains a list of the diners
# it is currently taking care of, and progresses them through the different stages of the
# restaurant. The waiter will repeat multiple cycles of attending to the
# diners. In each cycle, the waiter will seat a new diner, if one arrives, take any diners’
# orders if needed, and give diners their bill, according to each diner’s status

from Menu import Menu
from Diner import Diner


class Waiter:
    def __init__(self, menu):
        self.diners = []
        self.menu = menu

    # Add newly arrived Diner
    def addDiner(self, diner):
        self.diners.append(diner)

    # Return number of diners currently being served
    def getNumDiners(self):
        return len(self.diners)

    # Goes through each diner and prints where they are in the process
    def printDinerStatuses(self):
        numDiners = self.getNumDiners()
        print("\nDiners who are seated:")
        # Just seated Diners have a 0 status -- this pattern continues until leaving Diners have a status of 4
        for i in range(numDiners):
            if self.diners[i].getStatus() == 0:
                print("\tDiner " + self.diners[i].getName() + " is currently seated.")

        print("Diners who are ordering:")
        for i in range(numDiners):
            if self.diners[i].getStatus() == 1:
                print("\tDiner " + self.diners[i].getName() + " is currently ordering.")

        print("Diners who are eating:")
        for i in range(numDiners):
            if self.diners[i].getStatus() == 2:
                print("\tDiner " + self.diners[i].getName() + " is currently eating.")

        print("Diners who are paying:")
        for i in range(numDiners):
            if self.diners[i].getStatus() == 3:
                print("\tDiner " + self.diners[i].getName() + " is currently paying.")

        print("Diners who are leaving:")
        for i in range(numDiners):
            if self.diners[i].getStatus() == 4:
                print("\tDiner " + self.diners[i].getName() + " is currently leaving.")

    # Collects a Diner's full order when they are ready
    def takeOrders(self):
        numDiners = self.getNumDiners()
        for i in range(numDiners):
            # Only take orders of Diners with a status on 1 (ordering)
            if self.diners[i].getStatus() == 1:
                Menu.printMenuItemsByType(self.menu, "Drink")
                print(self.diners[i].getName() + ", please select a Drink menu Item number")
                drinkChoice = input("> ")
                # If invalid choice keep asking until proper response is received
                while not drinkChoice.isdigit() or int(drinkChoice) < 0 \
                        or int(drinkChoice) > len(self.menu.drinkList)-1:
                    drinkChoice = input("> ")
                    if drinkChoice.isdigit():
                        drinkChoice = int(drinkChoice)
                        # Check within range of number of menu items
                        if drinkChoice < 0 or drinkChoice > len(self.menu.drinkList)-1:
                            drinkChoice = input("> ")
                        else:
                            break
                if isinstance(drinkChoice, str):
                    drinkChoice = int(drinkChoice)
                print()
                # Once choice is validated, add the selected item to the specific Diner's order using the menu class
                self.diners[i].addToOrder(self.menu.drinkList[drinkChoice])

                Menu.printMenuItemsByType(self.menu, "Appetizer")
                print(self.diners[i].getName() + ", please select an Appetizer menu Item number")
                appetizerChoice = input("> ")
                # If invalid choice keep asking until proper response is received
                while not appetizerChoice.isdigit() or int(appetizerChoice) < 0 \
                        or int(appetizerChoice) > len(self.menu.appetizerList)-1:
                    appetizerChoice = input("> ")
                    if appetizerChoice.isdigit():
                        appetizerChoice = int(appetizerChoice)
                        # Check within range of number of menu items
                        if appetizerChoice < 0 or appetizerChoice > len(self.menu.appetizerList)-1:
                            appetizerChoice = input("> ")
                        else:
                            break
                if isinstance(appetizerChoice, str):
                    appetizerChoice = int(appetizerChoice)
                print()
                # Once choice is validated, add the selected item to the specific Diner's order using
                self.diners[i].addToOrder(self.menu.appetizerList[appetizerChoice])

                Menu.printMenuItemsByType(self.menu, "Entree")
                print(self.diners[i].getName() + ", please select an Entree menu Item number")
                entreeChoice = input("> ")
                # If invalid choice keep asking until proper response is received
                while not entreeChoice.isdigit() or int(entreeChoice) < 0 \
                        or int(entreeChoice) > len(self.menu.entreeList)-1:
                    entreeChoice = input("> ")
                    if entreeChoice.isdigit():
                        entreeChoice = int(entreeChoice)
                        # Check within range of number of menu items
                        if entreeChoice < 0 or entreeChoice > len(self.menu.entreeList)-1:
                            entreeChoice = input("> ")
                        else:
                            break
                if isinstance(entreeChoice, str):
                    entreeChoice = int(entreeChoice)
                print()
                # Once choice is validated, add the selected item to the specific Diner's order using
                self.diners[i].addToOrder(self.menu.entreeList[entreeChoice])

                Menu.printMenuItemsByType(self.menu, "Dessert")
                print(self.diners[i].getName() + ", please select a Dessert menu Item number")
                dessertChoice = input("> ")
                # If invalid choice keep asking until proper response is received
                while not dessertChoice.isdigit() or int(dessertChoice) < 0 \
                        or int(dessertChoice) > len(self.menu.dessertList)-1:
                    dessertChoice = input("> ")
                    if dessertChoice.isdigit():
                        dessertChoice = int(dessertChoice)
                        # Check within range of number of menu items
                        if dessertChoice < 0 or dessertChoice > len(self.menu.dessertList)-1:
                            dessertChoice = input("> ")
                        else:
                            break
                if isinstance(dessertChoice, str):
                    dessertChoice = int(dessertChoice)
                print()
                # Once choice is validated, add the selected item to the specific Diner's order using
                self.diners[i].addToOrder(self.menu.dessertList[dessertChoice])

                self.diners[i].printOrder()

    # Checks to see if any Diners are ready to pay and takes their money
    def ringUpDiners(self):
        numDiners = self.getNumDiners()
        for i in range(numDiners):
            if self.diners[i].getStatus() == 3:
                print("\n" + self.diners[i].getName() + ", your meal cost $" + str(self.diners[i].calculateMealCost()))

    # When a Diner is leaving this removes them from the queue since they no longer need a Waiter
    def removeDoneDiners(self):
        numDiners = self.getNumDiners()
        for i in range(numDiners-1, -1, -1):
            if self.diners[i].getStatus() == 4:
                print(self.diners[i].getName() + ", thank you for dining with us! Come again soon!")
                del self.diners[i]

    # Completes all the Waiter functions of taking orders, ringing up Diners, and saying goodbye to finished Diners
    def advanceDiners(self):
        self.printDinerStatuses()
        self.takeOrders()
        self.ringUpDiners()
        self.removeDoneDiners()
        numDiners = self.getNumDiners()
        # Updates all Diners still here to move them along
        for i in range(numDiners):
            self.diners[i].updateStatus()

