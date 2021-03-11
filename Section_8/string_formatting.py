# Let's talk formatting

# I want to concatentate some things!
# I've got all these variables and I need to use them in the below print example
thing = 'hello' + 'world'
name = 'Alice'
place = 'Main Street'
time = '6 pm'
food = 'turnip'
# Notice how complex it is in terms for formatting, it works, but it's not the best way to do this due to complexity.
print('Hello ' + name + ', you are invited to a party at ' + place + ' at ' + time + '. Please bring ' + food)

# To dddress this we have string formatting also known as string interpretation

print('Hello %s, you are invited to a party at %s at %s. Please bring %s.' % (name, place, time, food))
# In the above example you type the string as you normall would substituting %s for the variable names. 
# At the end of the string you add %, then in parenthesis list the variables in order of assignment.
