guests = ['Jidhu', 'Thouseef', 'Aravind']

# 3.4
message = "Hi " + guests[0] + " I invite u to the dinner tomorrow!"
print(message)

message = "Hi " + guests[1] + " I heartly welcome u to the dinner tomorrow."
print(message)

message = "Hi " + guests[2] + " I welcome u to the dinner tomorrow night."
print(message)

not_come = guests.pop(1)
print("the one who not came is " + not_come)
print(not_come)

guests.insert(1 , 'Anand')
message = "Hi " + guests[1] + " I welcome u to the dinner tonight."
print(message)
print(guests)

guests.insert(0, 'Vignesh')
message = "Hi " + guests[0] + " i just get the news that i got big table so ill invite to the dinner"
print(message)
print(guests)

guests.insert(2, 'balaji')
message = "Hi " + guests[2] + " I just got to know that i got big table so ill invite u to dinner"
print(message)
print(guests)

guests.append('vicky')
message = "Hi " + guests[-1] + " I got a news that we have a table for dinner so i invite u"
print(message)
print(guests)

not_come = guests.pop(-1)
print(guests)
print("the one again make a mess is " + not_come)
print(not_come)

guests.pop(3)
message = "sorry " + guests[3] + " i can't invite u, the table not confirmed"
print(message)
print(guests)

guests.pop(2)
message = "sorry " + guests[2] + " i can't invite u and table not confirmed"
print(message)
print(guests)

guests.pop(0)
message = "sorry" + guests[0] + " i cant make it tomorrow"
print(message)
print(guests)

print("the two people only invited and still in the list is " + guests[0] + " and " + guests[1])
print(guests)

del guests[0]
del guests[0]

print(guests)
