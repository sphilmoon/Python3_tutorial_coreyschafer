# sorting list:
# using sorted function is more flexible than using the method.

list_1 = [9, 2, 5, 3, 1, 8, 6, 4, 7]
sort_list1 = sorted(list_1)
sort_list1 = sorted(list_1, reverse = True) # descending order.

list_1.sort() # sorting my original without creating a variable.
list_1.sort(reverse = True) # descending order.

print('sorted variable:\t', sort_list1)
print('original variable:\t', list_1)

# sorting tuples:
tuple  = (9, 2, 5, 3, 1, 8, 6, 4, 7)
# tuple.sort() # this won't work. So use the sort function.
sorted_tuple = sorted(tuple)
print('sorted tuple:\t', sorted_tuple)

# sorting dictionaries also use the function, not the method:
dic = {'Name': 'Phil', 'Hobby': 'doing python', 'OS': 'Mac'}
sorted_dic = sorted(dic)
print('sorted dic:\t', sorted_dic)

# sorting based on different criteria:
list_2 = [-2, -5, -9, 0, 4, 1, 3]
sorted_list_2 = sorted(list_2, key = abs) # sorting based absolute values.
print(sorted_list_2)

# class sorting:
class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({}, {}, {})'.format(self.name, self.age, self.salary)

E1 = Employee('Carl', 37, 70000)
E2 = Employee('Katy', 29, 99000)
E3 = Employee('Jon', 40, 90000)

employees = [E1, E2, E3]

def E_sort(emp):
    return emp.salary
    # need a key values
sorted_employees = sorted(employees, key = E_sort, reverse = True)
print(sorted_employees)

    # using the lambda function:

sorted_employees = sorted(employees, key = lambda E: E.name)
print(sorted_employees)

    # OR using the attrgetter:
from operator import attrgetter

sorted_employees = sorted(employees, key = attrgetter('age'))
print(sorted_employees)
