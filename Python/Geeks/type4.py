# python demonstrates the type convertion
##dict(), complex(), str()

#initializing integer
a = 1
b = 2

#initializing tuple
tup = (('a', 1), ("f", 2), ('g', 3))

#printing integer converting to complex number
c = complex(1,2)
print("After converting integer to complex : ", end = '')
print(c)

#printing integer to string
s = str(a)
print("after converting integer to string : ", end = '')
print(s)

#printing tuple convertion to expression dicrionary
c = dict(tup)
print("After converting tuple to dictionary: ", end = '')
print(c)
