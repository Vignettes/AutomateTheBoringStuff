### String Methods ###

# First let's talk about pyperclip as it can copy to and from the clipboard.
# Install via pip "pip install pyperclip" in CMD on Windows, Terminal on Mac. 
# Then import it
import pyperclip

# To copy to the clipboard
pyperclip.copy('Hello!!!!!!!!!!!!')  # Copies Hello!!!!!!!!!!!! to the clipboard
# To paste from the clipboard
print(pyperclip.paste()) # Prints the contents of the clipboard. 


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

#'hello'.isalpha() = True isalpha() checks if it's alpha 
#'hello123'.isalnum() = True isalnum() checks if it's alpha an numeric
#'hello world'.isspace() = False as the string isn't a space BUT
#'hello world'[5].isspace() = True the 5th index is a space
#'This is a title case'.istitle() = False istitle() all words must start with a capitalization
#'Hello world'.title() = 'Hello World' makes both words capitalized at the start
#'Hello World'.endswith('world!) = FALSE ends with world != world!
#'Hello World'.startswith('Hello') = True starts with Hello


# Need to join together a list of strings?
test = ','.join(['Cats', 'Rats','Bats']) # adds , between each value in list. 
print(test)

# Need to split out a string to individual words in a list?
new = 'My name is Simon'.split() # Creates it as ['My', 'name', 'is', 'Simon']
print(new)
new = 'My name is Simon'.split('m') # Creates it as ['My na', 'e is Si', 'on']
print(new)


Hi = 'Hello'.rjust(10) # adds white space padding to right adjust
print(Hi)

Hi = 'Hello'.rjust(20, '*') # adds white space padding to right adjust, adds '*'  before text
print(Hi)

Hi = 'Hello'.ljust(10) # adds white space padding to left adjust
print(Hi)

Hi = 'Hello'.center(20, '=') #adds = before and after the text
print(Hi)

Hi = '    Hello' 
print(Hi.strip())  # removes the spaces in the string

Hi = '    Hi     '
print(Hi.lstrip()) #removes the spacing to the left

Hi = '    Hi     '
print(Hi.rstrip()) #removes the spacing to the right

# We can pass the strip method a string with characters to remove instead of whitespace
spam = 'SpamSpamBaconSpamEggsSpamSpam'.strip('ampS') # Removes capital S, p, a, and m. 
print(spam) # prints BacnSpamEggs because it removes the characters up to the first letter that wasn't passed to the string 

# Now tell me how I can replace some of the info in my string. 
# Just use .replace('to_be_replaced', 'to_replace')
spam = 'Hello There!' 
spam.replace('e', 'XYZ') # replace all instances of e with XYZ
print(spam)

