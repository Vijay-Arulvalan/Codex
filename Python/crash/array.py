# 3.1 Names
room= ['vijay', 'vignesh', 'balaji', 'jidhu', 'anand']
print(room[0].title())
print(room[1].title())
print(room[2].title())
print(room[3].title())
print(room[4].title())

# 3.2

message = "hello " + room[0].title() + "," " here are your roommates."
print(message)

message = "He is " + room[1]
print(message)

message = "He is " + room[2]
print(message)

message = "He is " + room[3]
print(message)

message = "And He is " + room[4]
print(message)

#one more method for 3.2
message = "They are " + room[1] + "," + room[2] + "," + room[3] + "," + room[4]+ "."
print(message)

# 3.3

tech = ['iphone', 'macbook pro', 'airpods', 'watch',]
print(tech)

message = "i would love to buy " + tech[1].title() + '.'
print(message)

message = "But before that i need to buy " + tech[3] + '.'
print(message)

message = "I don't know why but i like that and after that only " + tech[2] + " and " + tech[0] + " and then only " + tech[1].title() + "."
print(message)
