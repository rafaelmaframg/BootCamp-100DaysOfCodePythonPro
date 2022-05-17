#Day 2 Solution

#1. create the greting for the program
print('Welcome to the Tip Calculator.')

#2. ask the user fot the total bill
while True:
    try:
        total = float(input('What is the total bill?\n'))
        break
    except:
        print('Please, enter a valid number!')


#3. ask the user for the number of people to split the bill
while True:
    try:
        people = int(input('How many people to split the bill?\n'))
        break
    except:
        print('Please enter a valid number!')

#4. ask the user for the percentage of tip
while True:
    try:
        tip = int(input('What percent tip would you like to give? 10,12 or 15\n'))
        break
    except:
        print('Please, enter a valid number!')

#5. calculate
resultado = (total*(tip/100+1)) / people

#6. show the value per person
print(f'Each person should pay: ${resultado:.2f}')