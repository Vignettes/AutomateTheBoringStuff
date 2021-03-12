# Let's make a script to get directions

import webbrowser, sys, pyperclip

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed
if len(sys.argv) > 1:
   # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
   address = ''.join(sys.argv[1:]) # from index 1 to the end of the list join together to a string
else:
    address = pyperclip.paste() # takes whatever text is on clipboard and returns it as string
    
webbrowser.open('https://www.google.com/maps/place/' + address)

   