from os import system, name
import random


cards = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','J♥','Q♥','K♥',
'A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','J♦','Q♦','K♦',
'A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','J♣','Q♣','K♣',
'A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','J♠','Q♠','K♠']

def clear():
    #for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')



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
        if element[:2] == '10' or element[0] in 'JQK':
            sumof += 10
        elif element[0] == 'A':
            sumof += 11
        else:
            sumof += int(element[0])
    return sumof

def check_as(lista):
    for i in lista:
        if i[0] == 'A':
            return i[1]
    return False
