from art import logo
from Clear import clear

#1 show the logo
print(logo)
auction = {}
highest = 0
name = ''

#2 ask the name - input
#3 ask the bid price
#4 add name and bid into a dictionary as the key and value
#5 ask if there are other users who want to bid if yes clear the screen no find the highest bid in the dictionary
while True:
    try:
        name = str(input("What is your name?: "))
        price = int(input("What is your bid?: $"))
        auction[name] = price
        cont = str(input("Are there any other bidders? Type 'yes' or 'no'.\n")).lower()
        if cont == 'no':
            for key, value in auction.items():
                if value > highest:
                    highest = value
                    name = key
            break
        else:
            clear()
    except:
        print('Please, enter a valid data')

#6 show the winner
print(f"The Winner is {name} with a bid of ${highest}")



