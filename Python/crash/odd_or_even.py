number = input("Tell me the number and I'll tell you its odd or even: ")
number = int(number)

if number % 2 == 0:
    print('The number ' + str(number) + ' you said is even.')
else:
    print('The number ' + str(number) + ' you said is odd')
print('*************')
