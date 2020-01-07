# Strings and Text

types_of_people = 10
x = f"There are {types_of_people} types_of_people."

Binary = "binary"
Do_not = "don't"
y =f"Those who know {Binary} and those who {Do_not}."

print(x)
print(y)

print(f"I said: {x}.")
print(f"I also said: {y}")

hilarious = True
joke_evaluation = "isn't that joke funny! ? {}"

print(joke_evaluation.format(hilarious)) #here we use the format function in different way ..we use format inside ...

w = "This is the left side of "
q = "the right side of the string"

print(w+q)
