
# simple program for sms abbreviation translation 

import sys

oldies = {"ROFL": "Rolling On Floor Laughing",
         "LOL":   "Laughing Out Loud",
         "IMHO":  "In My Honest Opinion",
         "FYEO":  "For Your Eyes Only",
         "BTW":	  "By the Way",
         "SCNR":  "Sorry, could not Resist"}




def translate(abbreviated):
    if abbreviated in oldies:
        reformatted = oldies.get(abbreviated)
        print("Cool, thats here. The abbreviated version is --> '{0}' ".format(reformatted))

    elif KeyError:
        print("Sorry I don`t know that one!")
         
def addToList(new):
    pass


while True:

    try:
        abbreviated = input("Please enter the SMS abbreviation --> ").upper()
        if abbreviated == 'Q':
            sys.exit()
        else:
            translate(abbreviated)

    except Exception:
        print("Please enter a string not numbers")
        abbreviated = input("Please enter the SMS abbreviated").upper()
        translate(abbreviated)


    finally:
        print("Have another go! or type q to exit")


