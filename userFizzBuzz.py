a = int(input("Pick a number you would like to be Fizz: "))
b = int(input("Pick a number you would like to be Buzz: "))


def fizzbuzz(num1, num2):

    for x in range(1, 100):
        if x % a == 0 and x % b == 0:
            print("FizzBuzz")
        elif x % num2 == 0:
            print("Buzz")
        elif x % num1 == 0:
            print("Fizz")
        else:
            print(x)

fizzbuzz(a, b)