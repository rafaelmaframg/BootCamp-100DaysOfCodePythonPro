import random
from modules.clearfunction import clear
#ascii art for the hangman
from modules.art_hangman import logo, stages
from modules.hangmanwords import word_list


#greeting for the program
print("Welcome to:")
print(logo)


#1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
lives = 6
chosen_word = random.choice(word_list)

#2-create the blank lines with the lenght of chosen word
word_result = ['_' for i in range(len(chosen_word))]

#3 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while True:
    guess = str(input('Please, enter a letter:\n')).lower()
    clear()
    if guess in word_result:
        print(f"You've already guessed {guess} ")
    if guess in chosen_word:
        print('Right!\n')
        for n,letter in enumerate(chosen_word):
            if guess == letter:
                word_result[n] = guess
        print(' '.join(word_result))
        print(stages[lives])
    else:
        print('Wrong!\n')
        lives -= 1
        print(' '.join(word_result))
        print(stages[lives])

    if lives == 0:
        print('****************')
        print("*  YOU LOSE!   *")
        print('****************')
        print(f"The correct word is: {chosen_word}")
        break
    elif "_" not in word_result:
        print('****************')
        print('*  You WIN!!!  *')
        print('****************')
        break






