

# simple program for sms abbreviation translation (for old people!!)

import sys
import json

#oldies = {"ROFL": "Rolling On Floor Laughing",
#           "LOL": "Laughing Out Loud",
#           "IMHO": "In My Honest Opinion",
#           "FYEO": "For Your Eyes Only",
#           "BTW": "By the Way",
#           "SCNR": "Sorry, could not Resist"}

#with open("abbreviations.txt", 'w') as f:
#     json.dump(oldies, f, indent=4)
#     print("Abbreviation added")


def translate(abbreviated):
    with open('abbreviations.txt') as json_file:
        data = json.load(json_file)

    if abbreviated in data:
        reformatted = data.get(abbreviated)
        print("Thats here. The abbreviated version is --> '{0}' ".format(reformatted))

    elif KeyError:
        print("Sorry I don`t know that one!")


# def edit(newAbbreviation):
#     with open('abbreviations.txt', 'r') as file:
#         oldies = json.load(file)
#
#     output = "The current translation for {} is {}".format(newAbbreviation, oldies.get(newAbbreviation))
#     print(output)
#
#     choice = input('To edit this type e / E or to leave here and return to start type r / R').upper()
#     if choice == 'E':
#         addToList()
#     if choice == 'R':
#         return


def addToList():
    with open('abbreviations.txt') as file:
        oldies = json.load(file)

        newAbbreviation = input("Please enter the  SMS abbreviation first").upper()
        newvalue = input("And the human readable form")
        oldies.update({newAbbreviation: newvalue})
        file.close()

        with open('abbreviations.txt', 'w') as f:
            json.dump(oldies, f, indent=4)



    # newAbbreviation = input("Please enter the  SMS abbreviation first").upper()
    #
    # if oldies.get(newAbbreviation) is not None:
    #     print("This already exists, would you like to check or edit entry?, Y or N")
    #     choice = input("Y or N").upper()
    #
    # if choice == 'Y':
    #     # edit(newAbbreviation)
    #     print("add new")
    #
    # if choice == 'N':


while True:

    try:
        print("****************SMS TRANSLATOR******************")
        print("1 --> Translator")
        print("2 --> Add new abbreviation")
        print("3 --> Remove entry (coming Soon!)")
        print("************************************************")
        print("************************************************")

        selection = input("Please select an option  \n").upper()

        if selection == '1':
            abbreviated = input("Please enter the SMS abbreviation --> ").upper()
            translate(abbreviated)
        elif selection == '2':
            addToList()
        elif selection == '3':
            print("This feature has not been added yet!!")
        elif selection == 'Q':
            sys.exit()


    # except Exception:
    #     print("Please enter a string not numbers")
    #     abbreviated = input("Please enter the SMS abbreviated").upper()
    #     translate(abbreviated)

    finally:
        print("Have another go! or type q to exit")
