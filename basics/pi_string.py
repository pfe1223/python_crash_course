filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for lilne in lines:
    print(line.rstrip())
