def check(num):
    """
        The function to check the values and set the better design.
  
        Parameters:
            num (int): The number to check.
          
        Returns:
            (String): Return a string with the design.
    """
    if num == 11 or num == 1:
        num = 'A'
        dig = ' '
    elif num > 9:
        dig = num - 10
        num = 1
    else:
        dig = ' '
    return f'{num}{dig}'

def card(user, computer):
    """
        The function that receive the list of cards and return
        a string with the design of the ASCII cards.
  
        Parameters:
            user (list): The number list of user.
            computer (list) The number list of computer
          
        Returns:
            carta (string): a string that contains the result.
    """
    nipe = '♠'
    carta = f"""User {''.join(['      ' for x in range(len(user)+len(computer))])}      Computer
{''.join(['┌─────────┐' for x in user])}    {''.join(['┌─────────┐' for x in computer])}     
{''.join([f'│{check(x)}       │' for x in user])}    │░░░░░░░░░│{''.join([f'│{check(x)}       │' for x in computer[1:]])}
{''.join(['│         │' for x in user])}    │░░░░░░░░░│{''.join(['│         │' for x in computer[1:]])}
{''.join(['│         │' for x in user])}    │░░░░░░░░░│{''.join(['│         │' for x in computer[1:]])} 
{''.join([f'│    {nipe}    │' for x in user])}    │░░░░░░░░░│{''.join([f'│    {nipe}    │' for x in computer[1:]])}
{''.join(['│         │' for x in user])}    │░░░░░░░░░│{''.join(['│         │' for x in computer[1:]])}
{''.join(['│         │' for x in user])}    │░░░░░░░░░│{''.join(['│         │' for x in computer[1:]])} 
{''.join([f'│       {check(x)}│' for x in user])}    │░░░░░░░░░│{''.join([f'│       {check(x)}│' for x in computer[1:]])}
{''.join(['└─────────┘' for x in user])}    {''.join(['└─────────┘' for x in computer])}
 """
    return carta


def card_pc(user, computer):
    """
        The function that receive the list of cards and return
        a string with the design of the ASCII cards.
  
        Parameters:
            user (list): The number list of user.
            computer (list) The number list of computer
          
        Returns:
            carta (string): a string that contains the result.
    """
    nipe = '♠'
    carta = f"""User {''.join(['      ' for x in range(len(user)+len(computer))])}      Computer
{''.join(['┌─────────┐' for x in user])}    {''.join(['┌─────────┐' for x in computer])}     
{''.join([f'│{check(x)}       │' for x in user])}    {''.join([f'│{check(x)}       │' for x in computer])}
{''.join(['│         │' for x in user])}    {''.join(['│         │' for x in computer])}
{''.join(['│         │' for x in user])}    {''.join(['│         │' for x in computer])} 
{''.join([f'│    {nipe}    │' for x in user])}    {''.join([f'│    {nipe}    │' for x in computer])}
{''.join(['│         │' for x in user])}    {''.join(['│         │' for x in computer])}
{''.join(['│         │' for x in user])}    {''.join(['│         │' for x in computer])} 
{''.join([f'│       {check(x)}│' for x in user])}    {''.join([f'│       {check(x)}│' for x in computer])}
{''.join(['└─────────┘' for x in user])}    {''.join(['└─────────┘' for x in computer])}
 """
    return carta
