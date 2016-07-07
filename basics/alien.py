#Dictionary is a key value pair. You can use any object in Python
#as a key value pair (number, string, list, dictionary, etc.)

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#You can add new key value pairs to a dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

#You can modify the values in a dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(alien_0)

#Move the alien to the right
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	#This must be the fast alien
	x_increment = 3

#The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x-position: " + str(alien_0['x_position']))

#You can delete with - del alien_0['points']