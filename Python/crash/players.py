#Slicing is very important for example if we want to filter the top three players score in the list we can use Slicing

players = ['Cristiano', 'Messi', 'Neymer', 'Charles', 'Sachin', 'Dhoni']
print(players)
print(players[0:3]) #to slice the particular part in the list

#if we omit the first slicing python will start at first
print(players[:5])
print(len(players)) #to find the length of total list (len)

#if we want all the item from the third item of the list then we can omit the last object in print
print(players[3:])

#if we want to print last three in the list we can slice it by -
print(players[-3:])

print("\n\nHere are the first three players in my team: ")
for player in players[:3]:
    print(player.title())
