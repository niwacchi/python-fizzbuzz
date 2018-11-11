import sys

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

    return number

if __name__ == "__main__":
    for i in range(1, 20):
        print(fizzbuzz(i))
