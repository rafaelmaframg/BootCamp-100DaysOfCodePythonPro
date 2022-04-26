from functions import deal_card, sum_Of_elements, clear
from art.arts import card, card_pc


gameover = False

#start
#the user and computer should Each get 2 random cards
user = [deal_card(),deal_card()]
computer =  [deal_card(), deal_card()]

#the computer score was set outside of while to save memory
computer_score = sum_Of_elements(computer)

#oes the user orcomputer have a blackjack?
while not gameover:
    clear()
    print(card(user, computer))
    #Add up the user's and the computer's scores
    user_score = sum_Of_elements(user)
    if user_score == 21 or computer_score == 21:
        if user_score == 21:
            clear()
            print(card_pc(user, computer))
            print('<<< BlackJACK >>> - User WINN!!!')
            gameover = True
            continue
        else:
            clear()
            print(card_pc(user, computer))
            print('<<<  BlackJACK >>>> - Computer WINN!!')
            gameover = True
            continue

    #is user's score over 21?
    elif user_score > 21:
        #do they have an "Ace"
        if 11 in user:
            if (user_score -10) > 21:
                #If the ace counts as a 1 instead of 11, are they still over 21?
                clear()
                print(card_pc(user, computer))
                print('User LOSS')
                gameover = True
                continue
            else:
                user.remove(11)
                user.append(1)
                continue
        else:
            clear()
            print(card_pc(user, computer))
            print('User LOSS')
            gameover = True 
            continue
        #Ask the user if they want to get another card.
    
    answer = str(input(f'The sum of your cards is <<{user_score}>>, Do you want a new card?')).lower()
    #if answer yes... return to first conditional(while loop)
    if answer == 'yes': 
        user.append(deal_card())
        continue
    else:
    #Computer plays, if score is less than 17, keep drawing cards.
        while computer_score < 17:
            clear()
            print(card_pc(user, computer))
            computer.append(deal_card())
            computer_score = sum_Of_elements(computer)
            # Has computer gone over 21?
            if computer_score >= 21:
                if computer_score == 21:
                    clear()
                    print(card_pc(user, computer))
                    print('Black Jack - COmputer WiN')
                    gameover = True
                    continue  
                elif 11 in computer:
                    if (computer_score -10) > 21:
                        #If the ace counts as a 1 instead of 11, are they still over 21?
                        clear()
                        print(card_pc(user, computer))
                        print('User WIN')
                        gameover = True
                        continue

                    else:
                        computer.remove(11)
                        computer.append(1)
                        computer_score = sum_Of_elements(computer)
                        continue
                else:
                    clear()
                    print(card_pc(user, computer))
                    print('User WIN')
                    gameover = True
                    continue
        #Compare user score with computer score to see if user score is higher?
        if gameover:
            break
        elif computer_score > user_score:
            print('Computer WIN ')
        elif computer_score < user_score:
            print('User WIN')
        else:
            print('DRAW')
        break

