foods = ['pizza', 'cake', 'salad', 'burger', 'macroni']

friend_food = foods[:]
#to copy the whole list of foods to friend_food by slicing [:] it will cut from start till end of the list.
#if we not slice and copy the list then it will consider both as same list if we copy like this (foods = friend_food)

#to prove that we have two list we can add item to each list
foods.append('ice_cream')
friend_food.append('juice')

print("Here are my favorite foods: ")
print(foods)
print("\nHere are my friends favorite foods: ")
print(friend_food)

#if we want to copy the list make sure we can use the slice[:] to copy
