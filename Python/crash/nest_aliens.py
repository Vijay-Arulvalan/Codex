#alien_0 = {'color': 'green', 'points': 5}
#alien_1 = {'color': 'red', 'points': 10}
#alien_2 = {'color': 'blue', 'points': 15}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)

#create 30 alien generating :

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)

print('....')
print('Tolal number of aliens: ' + str(len(aliens)))
