### String Methods ###

# uppercase
spam = 'Hi'
print(spam.upper())

# to edit it

spam = spam.upper() # makes the variable upper

# lowercase

nope = 'HI'
print(nope.lower()) # prints lowercase version 

### Need to find out if a string is upper or lowercase?

print(spam.islower())  # will return the boolean to let you know if it is at least one lower
print(spam.isupper())  # will return the boolean to let you know if it is at least one upper

### You can validate with multiple methods passed

print(spam.upper().isupper())  # makes spam upper then returns boolean if it is upper.