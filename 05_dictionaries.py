# dictionary uses {} for keys and values - as a pair.
# string, integers, lists that are immutable.
ironman = {'name': 'Tony Stark', 'age': 40, 'skills': ['brain', 'handy']}
ironman['location'] = 24, 948, 293
ironman.update({'skills': 'big mouth'})

age = ironman.pop('age') #popping age key.

print(ironman.get('name')) # only the name.
print(ironman.get('location', 'Not Found')) # location, if not then 'Not Found'.
print(ironman) # all the items, except the age.
print(age) # print the popped message here.

print(len(ironman)) # printing how many keys are in my dictionary.
print(ironman.keys()) # number of key values.
print(ironman.values()) # only the values from the keys.
print(ironman.items()) # paring both keys and values.

for keys, values in ironman.items():
    print(keys, values)
