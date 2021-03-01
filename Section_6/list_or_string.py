# Many of the things you can do with lists you can also do with strings #

name = 'Zophie'
print(name[0]) #prints the Z from Zophie

# String values are immutable that cannot be changed, lists can be altered, they are mutable. #
# The proper way to create a new string is to use slices #

name = 'Zophie a cat'
newName = name[0:7] + ' the ' + name[8:12] #grabs Zophie and Cat not A and adds the.
print(newName)

spam = 5
cheese = ['hi', 'how', 'are', 'ya']
spam = cheese # creates a reference, if you edit one you will edit another because it has created a reference 
#Example below#

def eggs(cheese):
    cheese.append('Hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)


### To createa  complete seperate list you can use copy module and the deepcopy formula
import copy  # module to import to use deepcopy()

cheese = copy.deepcopy(spam) # create a new list that you can edit without altering the original version. 