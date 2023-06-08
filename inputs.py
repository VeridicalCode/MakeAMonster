# USER PROMPTS / INPUT

import valid as v

# get number of players, validate for valid INT
def getPartySize():
    loop = 1
    while loop != 0:
        num = v.get_integer("How many players in the party?\n")
        if num <= 0:
            print("Party size can't be zero or negative.")
        else:
            loop = 0
            return num
            
# get desired challenge rating, validate for valid FLOAT
def getTargetCR():
    loop = 1
    while loop != 0:
        CR = v.get_real("What challenge rating do you want the monster to have?\n")
        if CR < 0:
            print("Creatures must have a challenge rating of at least zero.")
        else:
            loop = 0
            return CR

# ask if the user wants a list of all prev monsters, y/n/yes/no
def promptForList():
    loop = v.get_y_or_n("\nWould you like to see a list of all monsters so far? (y/n)\n")
    return loop    

# ask if the user wants to go again, validate for y/n/yes/no
def promptForExit():
    loop = v.get_y_or_n("\nWould you like to make another monster? (y/n)\n")
    return loop