# For loops:
Letters = ['A', 'B', 'C', 'D', 'E']

for letters in Letters:
    if letters == 'B':
        print('Here!')
        break # this for_loop breaks when 'B' is found.
    print(letters)

# Continous statment:
Letters = ['A', 'B', 'C', 'D', 'E']

for letters in Letters:
    if letters == 'B':
        print('Here!')
        continue # continue statment resumes to the next iteration.
    print(letters)

# Loop within loop aka nested loops:
Letters = ['A', 'B', 'C', 'D', 'E']

for letters in Letters:
    for numbers in '123':
        print(numbers, letters)
        print(letters, numbers)

# built-in range function:
for i in range(11):
    print(i)

# While loop:
x = 3.14
while x < 10:
    print(x) # this will continue forever aka an infinite loop.
    x += 3 # x = x + 3. Additional condition to end the loop.

    # or

x = 22
while x < 50:
    if x == 42:
        break # this will stop when x meets 42, o/w loop continues til x hit 50.
    x += 5
    print(x)

    # if I want an infinite while loop:

x = 22
while True:
    # if x == 42:
    #    break
        x += 5
        print(x) # press ctrl+c to cancel the command.
