import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    global cards
    result = random.choice(cards)
    cards.remove(result)
    return result
#start
#the user and computer should Each get 2 random cards

user = [deal_card(),deal_card()]
computer =  [deal_card(), deal_card()]

#Add up the user's and the computer's scores
user_score = user[0] + user[1]
computer_score = computer[0] + computer[1]
print(computer_score , user_score)
#oes the user orcomputer have a blackjack?
if user_score == 21 or computer_score == 21:
    if user_score == 21:
        print('USER WINN')
    else:
        print('COmputer WINN')

#is user's score over 21?
else:
    if user_score > 21:
    #do they have an "Ace"
        if 11 in user and (user_score -10) > 21:
            #If the ace counts as a 1 instead of 11, are they still over 21?
            print('User LOSS')
    #Ask the user if they want to get another card.
    



print(user, computer)
print(cards)