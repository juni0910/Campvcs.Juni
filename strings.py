string = input("String: ")

ctr = 0
for i in string:
    ctr = ctr + 1
print(ctr)

print(len(string))

print(string[:3])
print(string[1:3])
print(string[3:])
print(string[-3:])

print(string[:3] + string[1:3] + string[3:1])
print(string[:3] * 3)


first = string[0]
ctr = 0
for i in string:
    if i == first:
        ctr = ctr + 1
print(ctr)

for i in string:
    if i % 2 == 0:
        print(i, end="")

#if we don't print the even, we are only printing the odd
#if odd: print charoctor