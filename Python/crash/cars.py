cars = ['bmw', 'audi', 'jaquar', 'toyoto', 'benz']
print(cars)

#if oncd it sorted there no turning back
cars.sort() #Ascending order
print(cars)

cars.sort(reverse=True) #Descending order
print(cars)

#here we can use sorted() to get into original order

print("\n Here is the original list: ")
print(cars)

print("\n Here is the sorted list: ")
print(sorted(cars))

print("\n Here is the original list again: ")
print(cars)

#reverse order #its not sort backward alphabetically it only reverse the list
print("\n\n Here is the reverse form of the list: ")
cars = ['bmw', 'audi', 'jaquar', 'toyoto', 'benz']
print(cars)

cars.reverse() #it permanently change the original order of the list but what we can do is we can reverse it in anytime.
print(cars)

#To find length of the list
print(len(cars))
