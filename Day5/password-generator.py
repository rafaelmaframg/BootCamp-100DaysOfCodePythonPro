#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

while True:
    try:
        nr_letters= int(input("How many letters would you like in your password?\n")) 
        nr_symbols = int(input(f"How many symbols would you like?\n"))
        nr_numbers = int(input(f"How many numbers would you like?\n"))
        type_password = int(input("What type of password would you like [1]-Easy [2]-Hard?\n"))
        if type_password < 1 or type_password > 2:
            print("Please, enter valid a valid number '1' or '2' for type password!")
        else:
            break
    except:
        print("Please, enter only numbers")

password = []

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for a in range(nr_letters):
    password.append(random.choice(letters))

for b in range(nr_symbols):
    password.append(random.choice(symbols))

for c in range(nr_numbers):
    password.append(random.choice(numbers))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
if type_password == 2:
    random.shuffle(password)

print(f"Your new password:\n {''.join(password)}")
    
