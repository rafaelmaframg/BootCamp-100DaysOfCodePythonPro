import sys

#1. add ASCII to program https://ascii.co.uk greeting for the program

tesouro = """# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=''_;=.______________|_____________________|_______
# |                   |  ,-''_,=''     `''=.|                  |
# |___________________|__'=._o`'-._        `'=.______________|___________________
#           |                `'=._o`'=._      _`'=._                     |
#  _________|_____________________:=._o '=._.'_.-='''=.__________________|_______
# |                   |    __.--' , ; `'=._o.' ,-'''-._ '.   |
# |___________________|_._'  ,. .` ` `` ,  `'-._'-._   '. '__|___________________
#           |           |o`'=._` , '` `; .'. ,  '-._'-._; ;              |
#  _________|___________| ;`-.o`'=._; .' ` '`.'\` . '-._ /_______________|_______
# |                   | |o;    `'-.o`'=._``  '` ' ,__.--o;   |
# |___________________|_| ;     (#) `-.o `'=.`_.--'_o.-; ;___|___________________
# ____/______/______/___|o;._    '      `'.o|o_.--'    ;o;____/______/______/____
# /______/______/______/_'=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__'=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____'=._o._; | ;_.--'o.--'_/______/______/______/_
# ____/______/______/______/______/_____'=.o|o_.--''___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/________
# *******************************************************************************"""

print(tesouro)

#2. ask the user for the direction:
while True:
    try:
        direction = str(input("You're at a crossroad. Where do you want to go? Type 'left' or 'right'\n")).lower()
        if direction == "left":
            break
        elif direction == "right":
            input("You fell into a hole. Game Over. Press enter to exit\n")
            sys.exit()
        else:
            print("Please, insert a valid answer! 'left' or 'right'\n")
    except SystemExit:
        sys.exit()
    except:
        print("Please, insert a valid answer! 'left' or 'right'\n")


#3.  ask the user for the action in the lake:
while True:
    try:
        lake = str(input("You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.\n")).lower()
        if lake == 'wait':
            break
        elif lake == 'swim':
            input("You get attacked by an angry trout. Game Over. Press enter to exit\n")
            sys.exit()
        else:
            print('Please, Insert a valid answer! "wait" or "swim\n"')
    except SystemExit:
        sys.exit()
    except:
        print('Please, Insert a valid answer! "wait" or "swim"\n')

#4. ask the user for the door color:
while True:
    try:
        color = str(input("You arrive at the island unharmed. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. Which colour do you choose?\n")).lower()
        if color == 'yellow':
            print("\n\nYou found the treasure! You Win!\n")
            break
        elif color == 'red':
            print("It's a room full of fire. Game Over!! Press enter to exit\n")
            sys.exit()
        elif color == 'blue':
            print("You enter a room of beasts. Game Over.\n")
            sys.exit()
        else:   
            print("Please, insert a valid answer! 'red', 'yellow', 'blue'\n")
    except SystemExit:
        sys.exit()
    except:
        print("Please, insert a valid answer! 'red', 'yellow', 'blue'\n")
 
