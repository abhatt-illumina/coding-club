# define a list using a function
shopping_list = list()
# define a list using the square brackets
another_list = ['apples', 3.3, 'pears', 'oranges', 2]
# add another element to the end
shopping_list.append('milk')
#slicing - returns a portion of the list
print(another_list[0:3])
# negative - -1 gives last element, -2 gives second last and so on
print(another_list[-1])
# remove last element
another_list.pop()
# add another element to the end of the list 
another_list.append('oranges')
# return the count of a certain value in the list
print(another_list.count('oranges'))
# concatenation
print(shopping_list + another_list)

#modify elements in a list
another_list[0] = 'peaches'
print(another_list)

# tuples 
coordinates = tuple()
print(coordinates)

names = ('Avni', 'Roberto', 1)
print(names)

#immutable - this will throw an error! 
print(names[0])
names[0] = 'Roberto'