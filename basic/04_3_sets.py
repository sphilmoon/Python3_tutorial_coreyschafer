# sets = values are not ordered without duplicats. Uses {}

mcu = {'iron man', 'captain america', 'thor', 'villains', 'spiderman'}
dcu = {'batman', 'villains', 'superman', 'wonder woman', 'aqua man'}

print('thor' in mcu) # Is it true?
print(mcu.intersection(dcu)) # print common item in both sets.
print(mcu.difference(dcu)) # print itmes only in the mcu set.
print(mcu.union(dcu)) # print all the items in both sets.

# creating empty sets
empty_set = {}  # This is incorret, since it is a built-in dictionary.
empty_set = set() # use this instead.
