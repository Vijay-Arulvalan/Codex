bicycles = ['trek', 'cannodale', 'redline', 'specialised']
print(bicycles) # to show the list bicycles
print(bicycles[1]) #to pull specific item in the list
print(bicycles[1].title()) #case for cannodale

print(bicycles[-1]) # -1 is for to pull the last item in the list
# -2 and -3 for the second and third item from the end of the list

message = "My first bicycle was a " + bicycles[2].title() + "."
print(message)

motorcycle = ['yamaha', 'Tvs', 'duke', 'pulzar']
print(motorcycle)

#modifying elements in the list
motorcycle[2] = 'ducati'
print(motorcycle)

#append (to add the new item to end of the list)
motorcycle.append('honda')
print(motorcycle)

#insert (to allocate the space for the item in particular space)
#this operation shift every item in the list to one step right
motorcycle.insert(0 , 'Royal Enfield')
print(motorcycle)
motorcycle.insert(2, 'Hero')
print(motorcycle)

#del (to delete any item from the list if we know the index)
del motorcycle[2]
print(motorcycle)

#pop (to remove the item in the list the gud thing in pop is we can use the removed item)
popped_motorcycles = motorcycle.pop() #we pop a item from the list and store it into popped_motorcycles.
print(motorcycle)
print(popped_motorcycles)

last_owned = motorcycle.pop()
print("I recently bought the motorcycle, which name is " + last_owned + ".")

# we can use pop to remove any item from the list if we know the index
first_owned = motorcycle.pop(0)
print("My first bike which i puchased was " + first_owned + ".")
# del is permanent and pop we can use that

#remove (sometimes we don't know the index of the list which we want ot delete but we know the value means we can use remove)
print(motorcycle)
motorcycle.remove('Tvs')
print(motorcycle)

too_expensive = 'ducati'
motorcycle.remove(too_expensive)
print(motorcycle)
print("\nA " + too_expensive + " is too expensive for me.")
#the remove method delete the value in first occurance if the value appear more than once in the list we need to use the list.
