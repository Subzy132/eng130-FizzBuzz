# Core:
# Write a program that prints the numbers from 1 to 100. For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz" instead of the number For numbers which are multiples of both three and five print "FizzBuzz".
# Extra:
# make a new fizzbuzz file and make it functional make it so we we can decide which numbers to substitute for fizz and buzz using functions
# Hint: loop, range, control flow

for x in range(1, 100):
    if  x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0:
        print("Fizz")
    else:
        print(x)