# A method is the same thing as a function except it is attached, or called onto a certain value #

spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') #index of the value hello

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower) #sorts it negating capitalization 
print(spam)