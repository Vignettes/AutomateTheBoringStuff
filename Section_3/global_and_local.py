spam = 42 #global variable (code in global scope can't use local variable)

def eggs():
    spam = 42 #local variable (can use global variables to read)
    
    
    
def spam():
    print(eggs) #checks for the variable and finds the global variable eggs
    
eggs = 42
spam()