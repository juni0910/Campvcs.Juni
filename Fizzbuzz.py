x = int(input("Number: "))
def fizzbuzz(x):

    if x % 3 == 0 and x%5==0:
        print("fizzbuzz")

    if x % 3 == 0:
        print("fizz", end="")

    elif x % 5 == 0:
        print("buzz")

fizzbuzz(x)