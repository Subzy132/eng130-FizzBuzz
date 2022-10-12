
a = int(input("Pick a number you would like to be Fizz: "))
b = int(input("Pick a number you would like to be Buzz: "))

for x in range(1, 100):
    if  x % a == 0 and x % b == 0:
        print("FizzBuzz")
    elif x % b == 0:
        print("Buzz")
    elif x % a == 0:
        print("Fizz")
    else:
        print(x)