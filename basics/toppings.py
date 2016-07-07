#Checks first to see if the list is empty. If not, lists all of the requested toppings.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza.")
else:
    print("Are you sure you want a plain pizza?")

#You can use multiple lists as well

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple',
                                      'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza.")
