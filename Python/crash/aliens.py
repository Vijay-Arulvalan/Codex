alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['x_position']= 0
alien_0['y_position'] = 12
#modifying
print("The alien color is " + alien_0['color'])

alien_0['color'] = 'Red'
print("The alien color is now " + alien_0['color'])

print(alien_0)

#deleting
del alien_0['points']
print(alien_0) #here the points is deleted permanently

# Using Empty dictionary

alien_1 = {}

alien_1['z_axis'] = 4
alien_1['y_axis'] = 8
alien_1['x_axis'] = 2

print(alien_1)
print('\n******************************')

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)
print("The original x_position is "+ str(alien_0['x_position']))

#alien_0['speed'] = 'fast' #to change the speed of alien in dictionary

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3


alien_0['x_position'] = alien_0['x_position'] + x_increment
print(alien_0)
print("The new x_position is " + str(alien_0['x_position']))
