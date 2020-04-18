alien_color = ['green', 'red', 'yellow']
print(alien_color)

alien = 'green'

#methods
if alien is 'green':
    print('You just earned 5 points')

else:
    print('You just earned 10 points')
#
alien = 'red'

if alien is 'green':
    print('You just earned 5 points')
elif alien is 'yellow':
    print('you just earned 10 points')
else:
    print('You just earned 15 points')

#

fruits = ['apple', 'orange', 'grapes', 'banana']
favorite_fruits = []
print(fruits)

if 'apple' in fruits:
    favorite_fruits.append('apple')
    print(favorite_fruits)
if 'berry' in fruits:
    favorite_fruits.append('berry')
    print(favorite_fruits)
if 'orange' in fruits:
    favorite_fruits.append('orange')
    print("\nMy favorite fruits are listed below \n")
    print(favorite_fruits)
