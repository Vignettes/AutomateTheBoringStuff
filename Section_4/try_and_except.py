def div42by(divideBy):
    try: #ties the following line of code
        return 42 / divideBy
    except ZeroDivisionError: #if prior try failed falls to except
        print('Error: You Tried to divide by zero')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


