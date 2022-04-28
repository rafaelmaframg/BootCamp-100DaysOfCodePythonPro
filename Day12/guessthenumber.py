import random

logo = """   ___                       _____ _                __                 _               
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|   """


#show greeting program
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = random.randint(1,100)

#ask about the difficulty easy or hard
difficulty = str(input("Choose a difficulty. Type 'easy' or 'hard'\n")).lower()
#set the attempts hard and easy
if difficulty == 'hard':
    print('You have 5 attempts to find the number')
    attempts = 5
else:
    attempts = 10
    print('You have 10 attempts to find the number')
while attempts > 0:
    #ask the user guess
    guess = int(input('Please, make a guess: \n'))
    
    if guess == answer:
        #win
        print(f"\nYou got it! The answer was {answer}.\n")
        break
    elif guess > answer:
        # too high
        print('\nToo High!!')
        attempts -= 1
        
    else:
        #too low
        print('\nToo low!!!')
        attempts -= 1
    if attempts == 0:
     print("You've run out of guesses, you lose.")
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")
        print('\nGuess again.\n')   





