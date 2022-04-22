#fizzbuzz solution

fizz_buzz = []

for num in range(1,100):
    if num % 3 == 0 and num % 5 == 0:
        fizz_buzz.append("FizzBuzz")
    elif num % 3 == 0:
        fizz_buzz.append("Fizz")
    elif num % 5 == 0:
        fizz_buzz.append("Buzz")
    else:
        fizz_buzz.append(str(num))

print(" ".join(fizz_buzz))
