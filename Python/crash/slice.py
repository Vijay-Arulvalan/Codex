# 4.10

colors = ['blue', 'green', 'gray', 'black', 'white', 'red', 'yellow']

print("The first three items in the list are: ")
print(colors[0:3])

print("The three items in the middle of the list are: ")
print(colors[2:5])

print("The last three in the list are: ")
print(colors[-3:])

# 4.11 My pizza your pizzas
pizzas = ['cheese', 'margarita', 'pepper corn']
friend_pizzas = pizzas[:]

print("\nI like this pizza and i forgot to tell: ")
pizzas.append('panneer')
print(pizzas)

print("My friend like this pizza: ")
friend_pizzas.append("chicken pizza")
print(friend_pizzas)

print("My favorite Pizzas are: ")
for pizza in pizzas:
    print(pizza)

print("My friend favorite pizza are: ")
for pizza in friend_pizzas:
    print(pizza)
