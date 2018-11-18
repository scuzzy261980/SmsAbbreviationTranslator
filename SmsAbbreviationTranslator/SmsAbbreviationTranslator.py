

# simple program for sms abbreviation translation (for old people!!)

import sys
import json

# open our abbreviations file and convert to dictionary
def translate(abbreviated):
    with open('abbreviations.txt') as json_file:
        data = json.load(json_file)

# check if the abbreviation entered exists in the dictionary and return the translated version or return key error
    if abbreviated in data:
        reformatted = data.get(abbreviated)
        print("Thats here. The human readable version of '{}'  is --> '{}' ".format(abbreviated, reformatted))

# cacth key error and return to start
    elif KeyError:
        print(" Sorry I don`t know that one!")

# remove an existing entry and save the new file
def remove():

    with open('abbreviations.txt') as file:
                oldies = json.load(file)
                file.close()

                selection = input("Which entry do you want to remove --> ").upper()
          
# if entry does not exist catch and return to start              
                if KeyError:
                    print("That entry does not exist!")

# if entry does exist, remove it
                else: del oldies[selection]

# save the dictionary to file
    with open('abbreviations.txt', 'w') as file:
                json.dump(oldies, file, indent=4)
                print("Entry has been removed")
               


# add a new entry to the dictionary
def addToList():
    with open('abbreviations.txt') as file:
        oldies = json.load(file)

        # take the user imput to add
        newAbbreviation = input("Please enter the  SMS abbreviation first --> ").upper() # convert abbreviations to uppercase
        newvalue = input("And the human readable form --> ").title() # capitalize the output for easy reading

# update the dictionary and save the file 
        oldies.update({newAbbreviation: newvalue})
        file.close()

   
    with open('abbreviations.txt', 'w') as f:
          json.dump(oldies, f, indent=4)
          print("--> Abbreviation Added Succesfully <--")

# main program

while True:

    try:
        print("****************SMS TRANSLATOR******************")
        print("1 --> Translator")
        print("2 --> Add new abbreviation")
        print("3 --> Show all current entries")
        print("4 --> Remove entry(feature not implemented yet)")
        print("q --> type q to quit")
        print("************************************************")
        print("************************************************")

        # user input for selection
        selection = input("Please select an option -->   \n").upper()

        # translate
        if selection == '1':
            abbreviated = input("Please enter the SMS abbreviation --> ").upper()
            translate(abbreviated)
        # add new entry
        elif selection == '2':
            addToList()
        # display current dictionary contents
        elif selection == '3':
             with open('abbreviations.txt') as file:
                oldies = json.load(file)
                print(oldies)
        # remove an entry from dictionary
        elif selection == '4':
             remove()
            
        # quit program
        elif selection == 'Q':
            sys.exit()
        # catch type error ( if anything other than a number is entered by the user
        elif TypeError:
            print("Please enter a NUMBER")

    # except Exception:
    #     print("Please enter a string not numbers")
    #     abbreviated = input("Please enter t
    #     he SMS abbreviated").upper()
    #     translate(abbreviated)



    finally:
        print("Have another go! or type q to exit")

