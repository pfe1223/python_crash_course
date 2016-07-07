#Make an empty list of aliens
aliens = []

#Make 30 green aliens
for alien_number in range(30):
	new_alien = {'color' : 'green', 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

for alien in aliens[0:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['points'] = 'medium'
		alien['points'] = 10
	elif alien['color'] == 'yellow':
		alien['color'] = 'red'
		alien['points'] = 'fast'
		alien['points'] = 15

#Show first 5 aliens
for alien in aliens[:5]:
	print(alien)
print("...")

#Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))