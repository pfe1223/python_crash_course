from random import randint
import pygal

def roll():
        return randint(1, 6)

results = []
for roll_num in range(1000):
        die1 = roll()
        die2 = roll()
        result = die1 + die2
        results.append(result)

frequencies = []
for value in range(2, 13):
        frequency = results.count(value)
        frequencies.append(frequency)

hist = pygal.Bar()

hist.title = 'Results of rolling two D6 1000 times'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')
