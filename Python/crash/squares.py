squares = [ ]
for value in range(1,11):
    square = value**2 #we store the every value of range in value and it **(exponents) 2 times and it store the output in square variable.
    squares.append(square) #here we append or add all the value of square in the empty list which we created on 1.

print(squares)

#Another method to print the square ..here we omit the additional variable square we created in previous

squares = []
for value in range(1,11):
    squares.append(value**2)
#we can reverse the value which going to print by "squares.insert(0, value**2)"
print(squares)

#Another method

squares = [value**2 for value in range(1,11)]
print(squares)
