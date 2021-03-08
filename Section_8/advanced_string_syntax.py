### Advanced String Syntax ###

# 'that is alice's cat ## doesn't work, invalid as text falls outside the string.
# "that is alice's cat" ## works, because the double quote allows a single quote character in it

# You can use escape characters to alter string. They start with \
    
   # 'Say hi to Bob \'s mother' # works, as the \ allows the single quote as part of the string
    

# \ single quote '
# \" double quote "
# \t tab
# \n new line
# \\ backslash

print('Hello there!\nHow are you?\nI\'m fine')

# You can use r to remove the need for those lines as it's a raw string

print(r"That is Carol's cat")

# You can use multiline strings with """"

print(""""Dear Alice,
Eve's cat has been arrested for cannapping, cat burglary, and extortion.
Sincerely,
Bob.""")