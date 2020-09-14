my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#        -10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# list[start:end:step]
print my_list[2:-1:2] # step print every second value.
print my_list[-2:-9:-2] # in reverse order with every second value.
print my_list[::-1] # in reverse order.


my_github = 'https://github.com/sphilmoon'
print my_github[::-1] # reverse url.
print my_github[-10:] # only my user domain.
print my_github[:-10] # excluding my user domain.
print my_github[8:] # excluding https://
