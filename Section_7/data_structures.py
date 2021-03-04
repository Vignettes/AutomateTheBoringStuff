import pprint

cat = {'name': 'Zophie',   # Initial dictionary
       'age': 7,
       'color': "gray"}

allCats = [] # Creating a list that is empty

allCats.append({'name': 'Zophie',   # Appending a dictionary into the list
       'age': 7,
       'color': "gray"})

allCats.append({'name': 'Pooka',   
                'age': 5,
                'color': 'black'})

print(allCats)


### Creating a tic-tac-toe board using data structures ###
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',  # Top row
            'mid-L': ' ','mid-M': ' ', 'mid-R': ' ',   # Middle row
            'bot-L': ' ','bot-M': ' ', 'bot-R': ' '}   # Bottom row

pprint.pprint(theBoard)

theBoard['mid-M'] = 'X'  # Places an X on the mid-M key.
pprint.pprint(theBoard)

theBoard['top-L'] = 'O'
theBoard['top-M'] = 'O'
theBoard['top-R'] = 'O'
theBoard['mid-L'] = 'X'
theBoard['low-R'] = 'X'
pprint.pprint(theBoard)

def printBoard(board):                                                               # Creating a function to display the board
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])            
    print('-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----')
    print(board['bot-L'] + '|' + board['bot-M'] + '|' + board['bot-R'])
    print('-----')
    
printBoard(theBoard) # Passes the values from theBoard to the printBoard function