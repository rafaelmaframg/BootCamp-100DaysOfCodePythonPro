def check(num):
    """
        The function to check the values and set the better design.
  
        Parameters:
            num (int): The number to check.
          
        Returns:
            (String): Return a string with the design.
    """
    if num == 11:
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
        a string with the design of the cards.
  
        Parameters:
            user (list): The number list of user.
            computer (list) The number list of computer
          
        Returns:
            carta (string): a string that contains the result.
    """
    nipe = '♠'
    carta = f"""User                                      Computer
┌─────────┐ ┌─────────┐      ┌─────────┐ ┌─────────┐
│{check(user[0])}       │ │{check(user[1])}       │      │░░░░░░░░░│ │{check(computer[1])}       │
│         │ │         │      │░░░░░░░░░│ │         │
│         │ │         │      │░░░░░░░░░│ │         │
│    {nipe}    │ │    {nipe}    │      │░░░░░░░░░│ │    {nipe}    │
│         │ │         │      │░░░░░░░░░│ │         │
│         │ │         │      │░░░░░░░░░│ │         │
│       {check(user[0])}│ │       {check(user[1])}│      │░░░░░░░░░│ │       {check(computer[1])}│
└─────────┘ └─────────┘      └─────────┘ └─────────┘"""
    return carta
