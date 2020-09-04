# First, the mutable for easy modification.
list_1 = ['frozen', 'thread', 'weakref', 'imp', 'warnings']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'
print(list_1)
print(list_2)

print('--------------------------------------------------')
# Second, not mutable for limiting modification.
# tupule = are not mutable.

tuple_1 = ['frozen', 'thread', 'weakref', 'imp', 'warnings']
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art'

print(tuple_1)
print(tuple_2)

# creating empty tuples
empty_tuple = ()
empty_tuple = tuple()
