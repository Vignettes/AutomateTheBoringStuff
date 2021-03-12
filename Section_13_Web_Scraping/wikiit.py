# Let's make a script to get directions

import webbrowser, sys, pyperclip

sys.argv 

# Check if command line arguments were passed
if len(sys.argv) > 1:
   lookup = ''.join(sys.argv[1:]) # from index 1 to the end of the list join together to a string
else:
    lookup = pyperclip.paste() # takes whatever text is on clipboard and returns it as string
    
webbrowser.open('https://en.wikipedia.org/wiki/' + lookup)

   