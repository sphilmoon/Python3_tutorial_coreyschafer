numbers = [2, 50, 33, 931, 16]
print(sum(numbers)) # printing the summation of numbers

courses = ['frozen', 'thread', 'weakref', 'imp', 'warnings']
print(courses.index('frozen'))
print('imp' in courses)

for item in courses: # creating a for loop,
    print(item) # indent basically means this command belongs to the for loop.

# enumerate function:
for index, item in enumerate(courses, start = 1):
    print(index, item)

# turn list into a string (joint):
courses_str = ' - '.join(courses)
print(courses_str)

# reversing back to the way it (split):
new_list = courses_str.split(' - ')
print(new_list)

# creating empty lists:
empty_list = []
empty_list = list()
