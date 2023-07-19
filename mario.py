# get the height from the user
# make height into an integer
h = int(input("height: "))

for i in range(1,h+1):
    print(" " * (h-i) + "#" * i)