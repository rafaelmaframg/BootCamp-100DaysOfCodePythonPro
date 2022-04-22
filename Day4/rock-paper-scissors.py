#importing random for computer choices
from random import randint


#ascii arts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#1. Start the game by asking the player:
while True:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
        if (choice < 0 or choice > 2):
            print('Please, enter a valid number, 1,2 or 3\n')
        else:
            break
    except:
        print('Please, enter a valid number, 1,2 or 3\n')
computer = randint(0,3)


##############################
#   1 Paper win 0 Rock       #
#   0 Rock win 2 Scissors    #
#   2 Scissors win 1 Paper   #
##############################

if choice == 0:
    if computer == 2:
        #user win rock / scissors
        print(rock)
        print("computer chose:")
        print(scissors)
        print("You WIN!!!")
        
    elif computer == 1:
        #computer win rock / paper
        print(rock)
        print("computer chose:")
        print(paper)
        print("You LOSE!")
    else:
        #draw  rock / rock
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a DRAW!")
elif choice == 1:
    if computer == 2:
         #computer win paper / scissors
        print(paper)
        print("computer chose:")
        print(scissors)
        print("You LOSE!")
    elif computer == 1:
        #draw  paper / paper
        print(paper)
        print("Computer chose:")
        print(paper)
        print("It's a DRAW!")
    else:
        #user win paper / rock
        print(paper)
        print("computer chose:")
        print(rock)
        print("You WIN!!!")
else:
    if computer == 2:
        #draw scissors / scissors
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("It's a DRAW!")
    elif computer == 1:
        #user win scissors / paper
        print(scissors)
        print("computer chose:")
        print(paper)
        print("You WIN!!!")
    else:
        #computer win scissors / rock
        print(scissors)
        print("computer chose:")
        print(rock)
        print("You LOSE!")
