# Use if-elif-else statements when you want to hav more than two possible
# outcomes. It runs each conditional until one is met. You can have more
# than one elif statement.

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

