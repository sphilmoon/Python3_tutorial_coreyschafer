# for locating my module then do:

# import sys
# sys.path.append('/Users/philmoon/Documents/Python')
# otherwise:

from imported_module_09 import find_index, test
import sys # locating where my module is imported from.

coffee = ['Americano', 'Latte', 'Capuccino', 'Machiatto']
index = find_index(coffee, 'Latte') # using find_index function.

print(index) # priting where 'Latte' is located.
print(test) # printing the test variable.
print(sys.path) # printing where my module is located at.
