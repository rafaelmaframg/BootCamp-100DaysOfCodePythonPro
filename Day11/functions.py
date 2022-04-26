from os import system, name
import random


cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

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
        sumof += element
    return sumof