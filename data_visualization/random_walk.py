import matplotlib.pyplot as plt 
from random import choice
from random import randint

def fill_x_values(walk_length):
	x_values = [0]
	points = walk_length
	while len(x_values) < points:
		x_direction = choice([1, -1])
		x_distance = choice([0, 1, 2, 3, 4])
		x_step = x_direction * x_distance
		next_x = x_values[-1] + x_step
		x_values.append(next_x)
	return x_values

def fill_y_values(walk_length):
	y_values = [0]
	points = walk_length
	while len(y_values) < points:
		y_direction = choice([1, -1])
		y_distance = choice([0, 1, 2, 3, 4])
		y_step = y_direction * y_distance
		next_y = y_values[-1] + y_step
		y_values.append(next_y)
	return y_values

walk_length = 50000 #input("How many points do you want for the walk?")
x_values = fill_x_values(walk_length)
y_values = fill_y_values(walk_length)
point_numbers = list(range(walk_length))

plt.scatter(x_values, y_values, c = 'red', edgecolor = 'none', 
	alpha = 0.2, s=7)

plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.figure(figsize=(10, 6))

plt.show()