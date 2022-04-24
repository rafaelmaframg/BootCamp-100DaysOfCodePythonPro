from art import logo


def add(a,b):
    """Return a sum of parameters a and b"""
    return a + b

def sub(a,b):
    """Return subtraction of a and b"""
    return a - b

def mult(a, b):
    """Return a multiply of a and b"""
    return a * b

def div(a, b):
    """Return a division of A and B and validate if B == 0"""
    if b > 0:
        return a / b
    else:
        return "Division by 0 is not possible"

#1. show logo
print(logo)
print('Welcome to the Calculator\n')

#2 ask for a number
while True:
    try:
        n1 = float(input('Please Insert the first number: '))
#3 ask for a operator
        op = str(input('Please select the operator \n + \n -\n *\n /\n'))
        if op not in "+-*/":
            print('Invalid operator! try again')
            continue
        #4 ask for the second number
        n2 = float(input('Please enter the second number: '))
        break
    except:
        print('Please enter a valid data')

operations = {'+': add, "-": sub, "*": mult, "/": div}



#5 show the result
print(f"{n1} {op} {n2} = {operations[op](n1, n2):.1f}")
