#printing printing

formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "hI, this is test the formatter files",
    "and i need to check how much complicate",
    "i can see in this code",
    "This may easy to understand or may be not"
))
