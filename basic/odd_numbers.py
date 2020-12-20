# printing odd numbers from the lists:
list1 = [9, 62, 52, 89, 101, 22]
list2 = [572, 85, 48, 137, 64]

# by using the modulus %:
print("These are the odd numbers:")
for num in list1:
    if num % 2 != 0:
        print(num)

# fiding the even numbers:
print("Now the even numbers:")
for num in list2:
    if num % 2 == 0:
        print(num)
