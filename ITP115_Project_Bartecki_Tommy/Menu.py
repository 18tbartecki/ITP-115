# This file defines the Menu class which will use MenuItem objects
# This class represents the restaurant’s menu which contains four different categories of
# menu items diners can order from.

from MenuItem import MenuItem


class Menu:
    MENU_ITEM_TYPES = ["Drink", "Appetizer", "Entree", "Dessert"]

    def __init__(self, fileName):
        self.drinkList = []
        self.appetizerList = []
        self.entreeList = []
        self.dessertList = []

        # Takes in a file and parses it until the respective lists
        fileIn = open(fileName, "r")
        for line in fileIn:
            line = line.strip()
            data = line.split(",")
            new_item = MenuItem(data[0], data[1], data[2], data[3])
            # Add menu items to menu list so Diner's can order from them
            if data[1] == "Drink":
                self.drinkList.append(new_item)
            elif data[1] == "Appetizer":
                self.appetizerList.append(new_item)
            elif data[1] == "Entree":
                self.entreeList.append(new_item)
            elif data[1] == "Dessert":
                self.dessertList.append(new_item)
        fileIn.close()

    # Used when a Diner selects a Menu item so they can add it to their order
    def getMenuItem(self, itemType, index):
        if itemType == "Drink":
            return self.drinkList[index]
        elif itemType == "Appetizer":
            return self.appetizerList[index]
        elif itemType == "Entree":
            return self.entreeList[index]
        elif itemType == "Dessert":
            return self.dessertList[index]

    # Nicely prints out the items for each category of food or drink
    def printMenuItemsByType(self, itemType):
        if itemType == "Drink":
            print("\n-----DRINKS-----")
            for index in range(len(self.drinkList)):
                print(str(index) + ") " + str(self.getMenuItem("Drink", index)))
        elif itemType == "Appetizer":
            print("-----APPETIZERS-----")
            for index in range(len(self.appetizerList)):
                print(str(index) + ") " + str(self.getMenuItem("Appetizer", index)))
        elif itemType == "Entree":
            print("-----ENTREES-----")
            for index in range(len(self.entreeList)):
                print(str(index) + ") " + str(self.getMenuItem("Entree", index)))
        elif itemType == "Dessert":
            print("-----DESSERTS-----")
            for index in range(len(self.dessertList)):
                print(str(index) + ") " + str(self.getMenuItem("Dessert", index)))

    # Returns the number of items of the specified type
    def getNumMenuItemsByType(self, itemType):
        if itemType == "Drink":
            return len(self.drinkList)
        elif itemType == "Appetizer":
            return len(self.appetizerList)
        elif itemType == "Entree":
            return len(self.entreeList)
        elif itemType == "Dessert":
            return len(self.dessertList)
