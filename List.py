food = ['pizza', 'chicken', 'fries']
number = [1, 2, 3]
mixed = ['pizza', 1, 'chicken', 2]

drinks = ['coke', 'smoothie', 'sprite']
menu = food+drinks
print(menu)

menu.remove('chicken')
print(menu)

menu.append('pasta')
print(menu)

menu.insert(0, 'hamburger')
print(menu)

menu.pop(6)
print(menu)

menu.sort()
print(menu)

menu.reverse()
print(menu)

print(menu[0])
print(menu[:2])

if "ice cream" in menu:
    print('sophie is happy')
else:
    print('sophie is sad')

food1 = input('food1: ')
food2 = input('food2: ')
food3 = input('food3: ')

order = []
order.append(food1)
order.append(food2)
order.append(food3)

print (order)

jellyctr = order.count('jelly')
print(jellyctr)