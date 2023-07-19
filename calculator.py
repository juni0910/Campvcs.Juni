print("Welcome to Juni's Calculator\n")

# get x and y from users
#define as integers
x = int(input("What is your first integer?"))
y = int(input("What is your second integer?"))

# get add, subtract, multiply or divide
math = input("What would you like to do with these number")

# if add,subtract, multiply or divde, computer answer
if math == "add":
    print(x, "+", y, "=", x+y)
elif math == "subtract":
    print(x, "-", y, "=", x-y)
elif math == "multiply":
    print(x, "*", y, "=", x*y)
elif math == "divide":
    print(x, "/", y, "=", x/y)

x=5
for i in range(3):
    x = x+1