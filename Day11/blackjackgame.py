import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """
        The function to randomize a "card" in the list and
        remove the choice from the list.
          
        Returns:
            result (Int): the card value.
    """
    global cards
    result = random.choice(cards)
    cards.remove(result)
    return result

def sum_Of_elements(lista):
    """
        The function to sum all the elements in the list.
  
        Parameters:
            lista (list): The list to be added.
          
        Returns:
            sumof (Int): int number that contains the sum.
    """
    sumof = 0
    for element in lista:
        print(element)
        sumof += element
    return sumof

#start
#the user and computer should Each get 2 random cards
user = [deal_card(),deal_card()]
computer =  [deal_card(), deal_card()]

#the computer score was set outside of while to save memory
computer_score = sum_Of_elements(computer)
print(f'User = {user} , Computer = {computer}')

#oes the user orcomputer have a blackjack?
while True:
    #Add up the user's and the computer's scores
    user_score = sum_Of_elements(user)
    if user_score == 21 or computer_score == 21:
        if user_score == 21:
            print('USER WINN')
            break
        else:
            print('COmputer WINN')
            break

    #is user's score over 21?
    elif user_score > 21:
        #do they have an "Ace"
        if 11 in user:
            if (user_score -10) > 21:
                #If the ace counts as a 1 instead of 11, are they still over 21?
                print('User LOSS')
                break
            else:
                continue
        else:
            print('User LOSS')
            break 
        #Ask the user if they want to get another card.
    
    answer = str(input(f'The sum of your cards is {user_score}, Do you want a new card?'))
    #if answer yes... return to first conditional(while loop)
    if answer == 'yes': 
        user.append(deal_card())
        continue
    else:
        break


print(user, computer)
print(cards)