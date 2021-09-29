# Tommy Bartecki, bartecki@usc.edu
# ITP 115, Fall 2020
# Assignment 9
# Description:
# This program translates a select list of words into other languages from English


def getLanguages(fileName="languages.csv"):
    fileIn = open(fileName, "r")
    # Reads first line of csv file to get headers
    line = fileIn.readline().strip()
    headers = line.split(",")
    # Removes English choice
    del headers[0]
    fileIn.close()
    return headers


def getSecondLanguage(langList):
    print("Translate English words to one of the following languages:")
    print("\t", end="")
    # Proper formatting for output of languages
    for languages in langList:
        print(languages, end=" ")
        if languages == "Italian":
            print("\n", end="\t")

    choice = input("\nEnter a language: ")
    choice = choice.strip()
    # Changing first letter to be uppercase
    finalChoice = choice[0].upper() + choice[1:len(choice)]
    # Continue until valid choice
    while finalChoice not in langList:
        print("This program does not support", finalChoice)
        choice = input("Enter a language: ")
        choice = choice.strip()
        finalChoice = choice[0].upper() + choice[1:len(choice)]

    return finalChoice


def readFile(langList, langStr="English", fileName="languages.csv"):
    fileIn = open(fileName, "r")
    # Removes header row
    header = fileIn.readline()
    finalWords = []
    column = 0
    # Finds proper column of words to look at
    for language in langList:
        if language == langStr:
            column = langList.index(language) + 1
    # Gets a list of words in second language
    for line in fileIn:
        line = line.strip()
        words = line.split(",")
        finalWords.append(words[column])
    fileIn.close()
    print(finalWords)
    return finalWords


def createResultsFile(language, resultsFile=None):
    # Makes default file name the chosen language
    if resultsFile is None:
        resultsFile = language + ".txt"
    fileOut = open(resultsFile, "w")
    fileOut.writelines("Words translated from English to " + language + "\n")
    fileOut.close()


def translateWords(englishList, secondList, resultsFile):
    fileOut = open(resultsFile, "a")
    translate = input("Enter a word to translate: ")
    choice = "y"
    # Loop to continue translating words until user is done
    while choice != "n" and choice != "N":
        # If not in English list keep asking for a new word
        while translate not in englishList:
            print(translate + " is not in the English list.")
            choice = input("Another word (y or n)? ")
            while choice != "y" and choice != "Y" and choice != "n" and choice != "N":
                choice = input("Another word (y or n)? ")
            if choice == "y" or choice == "Y":
                translate = input("\nEnter a word to translate: ")
            else:
                translate = englishList[0]
        # If user wants to keep entering words
        if choice != "n" and choice != "N":
            # Get the matching words by index
            index = englishList.index(translate)
            translatedWord = secondList[index]
            # If there is no translation
            if translatedWord == "-":
                print(translate + " did not have a translation.")
                choice = input("Another word (y or n)? ")
                while choice != "y" and choice != "Y" and choice != "n" and choice != "N":
                    choice = input("Another word (y or n)? ")
                if choice == "y" or choice == "Y":
                    translate = input("\nEnter a word to translate: ")
                else:
                    translate = englishList[0]
            else:
                # Otherwise output translation to user and to file
                print(translate + " is translated to " + translatedWord)
                fileOut.writelines(translate + " = " + translatedWord + "\n")
                choice = input("Another word (y or n)? ")
                # Ask if user would like to continue
                while choice != "y" and choice != "Y" and choice != "n" and choice != "N":
                    choice = input("Another word (y or n)? ")
                if choice == "y" or choice == "Y":
                    translate = input("\nEnter a word to translate: ")
                else:
                    translate = englishList[0]
    fileOut.close()


def main():
    print("Language Translator")
    headers = getLanguages("languages.csv")
    secondLanguage = getSecondLanguage(headers)
    englishWords = readFile(headers)
    foreignWords = readFile(headers, secondLanguage, "languages.csv")
    fileOut = input("Enter a name for the results file (return key for Finnish.txt): ")
    # If user just clicks enter for their file name
    if fileOut == "":
        fileOut = secondLanguage + ".txt"
    createResultsFile(secondLanguage, fileOut)
    translateWords(englishWords, foreignWords, fileOut)
    print("\nTranslated words have been saved to " + fileOut)


main()
