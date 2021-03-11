# In this lesson we will be dealing with pattern matching and regular expression

# Regular expressions allow you specify a pattern of text to search for, such as a phone number.
# Phone numbers are in the format 415-555-0000 (3-3-4)

def isPhoneNumber(text):
    if len(text) != 12:
        return False # not the regular length of a phone number
    for i in range(0,3):
        if not text[i].isdecimal():
            return False # no area code present
    if text[3] != '-':
        return False  # missing dash
    for i in range(4,7):
        if not text[i].isdecimal():
            return False # no first 3 digits
    if text[7] != '-':
        return False # missing second dash
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last 4 digits
    return True # returns true if all phone number criteria is met
        
print(isPhoneNumber('415-555-1234')) # prints True/False for the provided string
print(isPhoneNumber('hello')) # False, as this is not a phone number.

# The above is kind of long, but it works.

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line'
foundNumber = False # make a variable that starts as false to change to true when number found
for i in range(len(message)):
    chunk = message[i:i+12] # new variable chunk slices i to i + 12 indexed characters for each i value in length of message.
    if isPhoneNumber(chunk): # calls the function to look for a phone number on the variable chunk
        print('Phone number found: ' + chunk) # if a phone number is found prints the phone number
        foundNumber = True # sets foundNumber to True 
if not foundNumber: # if foundNumber remains False 
    print('Could not find any numbers.') # print that no numbers could be found
    
# The above is still kind of long, and uses another function, but is still useable.

# But let's use regular expressions!
import re # imports the regular expression module
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # set raw string, we are looking for d = digit, in the format passed to re.compile()
mo = phoneNumRegex.search(message) # variable mo set to search variable message for the format of phoneNumRegex
print(mo.group()) # returns the result, will grab the first found result. 

# Suppose we want to find all occurance?
# Eash there, just use .findall()
print(phoneNumRegex.findall(message)) # prints the found matches using phoneNumRegex on variable message. 
