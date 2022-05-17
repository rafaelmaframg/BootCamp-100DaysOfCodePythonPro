from art import logo, vs
from gamedata import data
import random
from os import name, system


def clear():
    '''Function to clear the screen'''
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


score = 0
choice_A = ''
choice_B = ''
gameover= False



while not gameover:
    clear()
    #show logo
    print(logo)
    
    if score > 0:
        print(f"You're right! Current Score: {score}")
    
    #show a random data A
    if choice_B != '':
        choice_A = choice_B
    else:
        choice_A = random.choice(data)
    print(f"Compare A: {choice_A['name']},a {choice_A['description']}, from {choice_A['country']}")
    #show VS
    print(vs)

    #show a random data B
    choice_B = random.choice(data)
    while choice_B == choice_A:
        choice_B = random.choice(data)

    print(f"Compare B: {choice_B['name']},a {choice_B['description']}, from {choice_B['country']}")

    #define the correct answer
    if choice_A['follower_count'] > choice_B['follower_count']:
        answer = 'A'
    else:
        answer = 'B'


    #ask higher
    user_choice = str(input("Who has more folllowers ? Type 'A' or 'B' :  ")).upper()

    #if right score +1 and new choices
    if user_choice == answer:
        score += 1
    else:
        gameover = True

print(f"Sorry, that's wrong. Final Score: {score}")



