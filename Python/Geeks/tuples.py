# use tuples, Dictionary, lambda

a, b = 10, 20

#using tuples to select the value
print((b , a) [a < b])

#using Dictionary to  select the value
print({True: a, False: b} [a < b])

#using lambda to select the value
print((lambda: b, lambda: a) [a < b] ())
