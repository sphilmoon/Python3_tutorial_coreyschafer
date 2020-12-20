message = 'Hello Phil\'s World'

print (len(message)) # print out the number of length or character.

print(message[0:14]) # this is called 'Slicing'.

# Method and function. method is a function that belongs to an object.

print(message.find('World')) # find the and argument.

message = message.replace('World', 'Universe') # return statement.
print(message)

greeting = "hello"
name = "phil"

message_2 = greeting + ', ' + name + ". Welcome!"

message_2 = '{}. {}. Welcome!'.format(greeting, name) # place holder.

print(message_2)

# formated string.

message_2 = f'{greeting.upper()}, {name}. Welcome!' # f string.
print(message_2)

print(help(str.upper) # string help instruction. 
