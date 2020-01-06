# if else without ternary operator
a = 10
b = 20
c = 30 

if a!=b & a!=c:
    if (a>b) & (a>c):
        print("a is greater")
    if (b>a) & (b> c):
        print("b is greater")
    else:
        print("C is greater")
else:
    print("A and B are equal")
