# create a Module to use this function to other scripts or in other modules.
# so then, import this Module by creating another Module.

print('Imported my_module!')

test = 'Test string'

def find_index(to_search, target): # this function includes two args.
    '''Finding the index of a value in a sequence.'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1
