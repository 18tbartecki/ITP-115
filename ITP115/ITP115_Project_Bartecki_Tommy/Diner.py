# This file defines the Diner class which represents one of the
# diners at the restaurant and keeps tracks of their status and meal

from MenuItem import MenuItem


class Diner:
    def __init__(self, name):
        self.name = name
        self.order = []
        self.status = 0

    # Moves Diner through the eating proceess
    def updateStatus(self):
        self.status += 1

    # Adds a Diners choice to their order
    def addToOrder(self, item):
        self.order.append(item)

    # Outputs a Diner's full order to console
    def printOrder(self):
        print(self.name + " ordered:")
        for i in range(len(self.order)):
            print("- " + str(self.order[i]))

    # Totals the cost of each ordered item for the bill
    def calculateMealCost(self):
        cost = 0
        for i in range(len(self.order)):
            cost += float(self.order[i].getPrice())
        return cost

    # Prints out what stage the Diner is in of dining at the restaurant
    def __str__(self):
        if self.status == 0:
            return "Diner " + self.name + " is currently seated"
        elif self.status == 1:
            return "Diner " + self.name + " is currently ordering"
        elif self.status == 2:
            return "Diner " + self.name + " is currently eating"
        elif self.status == 3:
            return "Diner " + self.name + " is currently paying"
        elif self.status == 4:
            return "Diner " + self.name + " is currently leaving"

    # Getter methods to acceess Diner's variables in other classes
    def getName(self):
        return self.name

    def getOrder(self):
        return self.order

    def getStatus(self):
        return self.status
