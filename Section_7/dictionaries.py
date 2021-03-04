### Dictionaries ###

# Like a list, they are a collection of many values. But, unlike listed indexes they can use many different data types
# not just integers. They have key-value pairs.

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'} # key is size, value is fat. separate each one with a comma.

# Access a keys value

myCat['size'] # Gives the value from size.

print(f"My cat has {myCat['color']} fur") #p prints my cat has gray fur taken from the dictionaries key-value pair. 

# In lists the values have to be organized for comparison 
[1, 2, 3] == [3, 2, 1] # This would be false, as the values are the same, but the ORDER is not.

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
ham = {'age': 8, 'name': 'Zophie', 'species': 'cat'}
print(eggs == ham) # This would be true as the values are the same, order does not matter. 

# You can use in and not in to check for values in a dictionary.

'name' in eggs # True

# Dictionaries are mutable, like list, they hold references.

# You can use list(variable.keys()) to get a list of the keys
print(list(eggs.keys()))
# You can use list(variable.values()) to get the values in the dictionary
print(list(eggs.values()))
# You can use list(variable.items()) to get the key-value pair in the dictionary
print(list(eggs.items()))

# You can use this in for loops

for k in eggs.keys(): #  loops over the keys in eggs and prints
    print(k)
    
for k, v in eggs.items(): # assign two variables one for key one for value, loops over the dictionary and prints
    print(k, v)
    
for i in eggs.items(): # assigns one variable, loops over the dictionary and prints in a tuple
    print(i)
    
# You can use .get() to look up a key and retrieve the default value it returns if the key value doesn't exist
# In get you format this way .get(key_to_look_up, value_to_return_if_doesn't_exist)
print(eggs.get('age', 0)) # returns value if age exists, if it doesn't returns 0.