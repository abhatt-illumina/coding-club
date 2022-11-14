# define a for loop in range
# 0 1 2 
for foo in range(3):
    print('this is foo: ', foo)

# for loop with data structure and control flow
numbers = [1, 2, 50, 9]
for number in numbers:
    if number%2 == 0:
        print('your number ', number, 'is even')
    else:
        print('your number ', number, 'is odd')

# another for loop with a data structure and control flow
shopping_list = ['orange', 1, 'milk', 40]
prices = []
items = []

for thing in shopping_list:
    if type(thing) == int:
        prices.append(thing)
    elif type(thing) == str:
        items.append(thing)
    else:
        print('this item is not supported!')

print('my prices', prices)
print('my items', items)