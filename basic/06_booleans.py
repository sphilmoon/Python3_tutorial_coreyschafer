# If statement can only define one at a time.

language = 'python'
language_2 = 'java'

# When it is true:
if language == 'python':
    print('The language is python')
else:
    print('No match')

# When it is false:
if language == 'java':
    print('The language is python')
else:
    print('No match')

# When it has multipe ifs/conditions:
# When it is true:
if language_2 == 'python':
    print('The language is python')
elif language_2 == 'java':
    print('The language is java')
else:
    print('No match')

# Switch-case scenario: just keep adding elif
if language_2 == 'python':
    print('The language is python')
elif language_2 == 'java':
    print('The language is java')
elif language == 'javascript':
        print('The language is javascript')
elif language == 'c++':
        print('The language is c++')
else:
    print('No match')

user = 'Administrator'
logged_in = True

if user == 'Administrator' and logged_in:
    print('Please log in')
else:
    print('Bad credentials')

if not logged_in:
    print('Please log in')
else:
    print('Welcome!')

# is and == are different.
a = [1, 2, 3]
b = [1, 2, 3]
a = b
print(a is b)

# false values:
# False
# None
# Zero
# Any empty sequence such as '' () []
# Any empty mapping such as {}
# Anything else is True.
condition = []

if condition:
    print('Evaluated to True!')
else:
    print('Evaluated to False!')
