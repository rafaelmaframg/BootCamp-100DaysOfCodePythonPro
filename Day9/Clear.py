from os import system, name

def clear():
    #for windows
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')