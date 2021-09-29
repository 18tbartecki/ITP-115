# This file defines the MenuItem class
# A MenuItem  represents a single item that a diner can order from the restaurant’s menu


class MenuItem:
    def __init__(self, name, itemType, price, description):
        self.name = name
        self.itemType = itemType
        self.price = price
        self.description = description

    # Prints a menu item and its price and description
    def __str__(self):
        return self.name + " (" + self.itemType + "): $" + str(self.price) + "\n\t" + self.description

    # All getters and setters to change and use the MenuItem variables in different classes
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getItemType(self):
        return self.itemType

    def setItemType(self, itemType):
        self.itemType = itemType

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description
