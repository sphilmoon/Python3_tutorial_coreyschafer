# Always start with def.
# Input and output.
def hello_func(): # add parameter in ().
    print('Hello Function.')    # adding a message.
hello_func() # to run my function.
hello_func()
hello_func() # easy to repeat and fix. # Keeping the code DRY.
                                       # Don't Repeat Yourself.

def second_func():
    return 'the second function.' #RETURN equals to the string itself.
print(second_func().upper()) # this returns as a string. Use a string method.

# Passing argument to our function:
#greeting variable is only scopes local function.
def third_func(greeting, name = 'You'):
    return '{}, {} = the Third Function.'.format(greeting, name)
print(third_func('hi', name = 'Phil'))

# Allowing arbitrary positional/keywords arguments.
def student_info(*args, **kwargs):
    print(args) # making an ARGS a tuple.
    print(kwargs) # dictionary with a keyworkd value.

courses = ['Art', 'Math'] # creating a list not a tuple.
info = {'name' : 'Phil', 'age': 22} # creating a dictionary.
student_info(*courses, **info) # * unpacks the value and print individually.

# examples:

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    """Return True for leap years, False for non-leap years."""
    # doc strings explain what this function does.

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month): # year and month argument.
    """Return number of days in that month in that year."""

    # year 2019
    # month 2
    if not 1 <= month <= 12: # the month has to be 1 thru 12.
        return 'Invalid Month'

    if month == 2 and is_leap(year): # using the function on the top.
        return 29

    return month_days[month] # print the actual number of days in that month

print(days_in_month(2019, 2))
