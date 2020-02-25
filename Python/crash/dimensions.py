#tuple

#tuple is like list except parenthasis... once we define items we can have access to it like list but we can't change that.
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# python does not allow you to change the tuple value
# dimensions[9] = 250

#using loop in tuple
print("\n")
for dimension in dimensions:
    print(dimension)

print("\n")

#we can't modify a tuple but we can reassign a new value to the entire tuple
dimensions = (200, 50)
print("Original dimensions: ")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\n Modified dimensions: ")
for dimension in dimensions:
    print(dimension)

#When compared to list tuple is simple data structure. use them when we want to store the value which cannot be changed though life of the program
