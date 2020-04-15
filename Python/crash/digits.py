#4.3 and 4.4 and 4.5
num = []
for value in range(1,21):
    num.append(value)
print(num)
print(min(num))
print(max(num))
print(sum(num))

#4.6

odd_num = list(range(1,21,2))
print(odd_num)

#another method

for value in range(1,21,2):
    print(value)

#4.7
threes = []
for value in range(3,31):
    threes.append(value*3)
print(threes)

#4.8
cubes = []
for value in range(1,11):
    cubes.append(value**3)
print(cubes)
