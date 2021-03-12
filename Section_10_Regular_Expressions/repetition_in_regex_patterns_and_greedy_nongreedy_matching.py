### You may want to match a certain number of repetitions of a group, such as if it appears more than 7 times but less than 10 ###

import re

batRegex = re.compile(r'Bat(wo)?man') # Looking for Bat(wo)man with the ? it means 1 or 0 times in the pattern to match
mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # Prints Batman 

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # Prints Batwoman


# mo = batRegex.search('The Adventures of Batwowowoman')
# print(mo.group()) # Error NoneType as it does not match

# Let's return the the phone number example

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-1234. Call me tomorrow')
print(mo.group()) # Prints the string for the number, but if the area code wasn't there it won't print anything. 

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d') # adding the () around the area code and the ? matches if it appears once or zero times
mo = phoneRegex.search('My phone number is 555-1234. Call me tomorrow') # Try changing this to 727-555-1234. It will still work. 
print(mo.group()) # This will print the number without the area code if it is not present, or with it if it is present. 

 
 # The asterisk means to match 0 or more times *     
batRegex = re.compile(r'Bat(wo)*man') # Looking for Bat(wo)man with the * it means at least 0 or more times in the pattern to match
mo = batRegex.search('The Adventures of Batwowowowowoman')
print(mo.group()) # Prints Batwowowowoman as it matches 0 or more times 

# The + character means match 1 or more, the group preceeding a plus must appear at least once
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The Adventures of Batman') # no match
mo = batRegex.search('The Adventure of Batwowowoman') # Works because the (wo) group appears 1 or more times. 

# What if I want to match a specific number of times?
haRegex = re.compile(r'(Ha){3}') # {num} for the number of times to match
print(haRegex.search('He said HaHaHa'))

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(, )?){3}') # Looking to match 3 phone numbers in a row with an optional comma (,)?
mo = phoneRegex.search('My numbers are 415-444-2223, 424-222-3345, 882-232-5555')
print(mo.group()) # returns the phone numbers sepearated by a comma 

# With the {} match number you can use formats like {1,5} similar to index slicing

digitRegex = re.compile(r'(\d){3,5}') # between 3-5 matches
print(digitRegex.search('1234567890'))
 
# By default Python runs greedy matches where it tries to match the most. For non-greedy add ? to the end of the pattern

digitRegex = re.compile(r'(\d){3,5}?') # The ? at the end of the {} notes to be non-greedy and it would grab the first 3 digits
print(digitRegex.search('1234567890'))