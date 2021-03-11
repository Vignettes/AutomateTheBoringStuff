# These are some of the more powerful pattern matching capabilities

# Say we want to sepearate the area code from a phone number.

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 414-555-4242')

# Now say we just want a section of the data in phoneNumRegex?
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # We've added () around the first grouping of \d\d\d to grab only the area code
mo = phoneNumRegex.search('My number is 414-555-4242')
# We put a second set of () around the other values to differentiate them
print(mo.group()) # Would print the full group
# What if I want to just get the first group?
print(mo.group(1)) # Prints only 414 as it is from the first group.

# If we had () in the phone number itself we need to escape those in order to search.
phoneNumRegex = re.compile(r'\(\d\d\d\)-\d\d\d-\d\d\d\d')  # The \ is used to escape the () at start and end for the evaluation.
mo = phoneNumRegex.search('My number is (414)-555-4242')
print(mo.group())


# Search variations of a term using pipes
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')   # re.compile(r'term(variation_1|variation_2|variation_3))
mo = batRegex.search('Batmobile lost a wheel') # Searches mo for batman, batmobile, batcopter, or bat
print(mo.group()) # Prints what it has found. 

# If the search pattern can't find what you're looking for it will return none. 