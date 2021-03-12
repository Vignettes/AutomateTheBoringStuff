### Files and folders and how Python can work with them ###
# If you want your data to persist after your program has finished, you need to save it to a file.

# Root folder C:\ on Windows
# Root folder / on Mac

# To use backslaches use \\ or use r in your string

# We should import OS to work with filepaths

import os

print(os.path.join('folder1', 'folder2', 'folder3', 'file.png')) # os.path.join() will combine the values to createa  file path agnostic to OS

# You can get your current working directory with os.getcwd()

print(os.getcwd()) # Prints the working directory that is current

os.chdir('c:\\') # to move to new working directory

# There are absolute filepaths which begin with the root folder C:/Folder/File
# Relative filepaths can begin with other folders, but it does not start with root  /Folder/File

# There are also . and .. folders that can be used in relative filepaths. 
# . = this folder 
# .. = parent folder ..\ is equal to C:/

# Need to get the absolute path for something?
os.path.abspath('spam.png') # would return the absolute path for spam.png in the folder

# You can check if a path is absolute by using os.path.isabs()
os.path.isabs('..\\..\\spam.png') # Would be false as this is not an absolute path 

# You can use os.path.relpath to get the relative path between two paths you provide
os.path.relpath('c:\\folder1\\folder2\\spam.png', 'c:\\folder1') # gives a relative path from the starding path c:\\folder1, to the first provided path

# If you just want the directory name you can use os.path.dirname()
os.path.dirname('c:\\folder1\\folder2\\spam.png') # Will return only directory c:\\folder1\\folder2

# If you just need the basename 
os.path.basename('c:\\folder1\\folder2\\spam.png') # Will return spam.png as it is after the final slash

# If you want to check if the file exists os.path.exists()
os.path.exists('c:\\folder1\\test.png') # Will return False unless you have that path

# You can also use os.path.isfile()
os.path.isfile('c:\\windows\\system32\\file.jpg') # False if the file isn't that

# You can check if for a directory with os.path.isdir
os.path.isdir('c:\\windows\\systemamfasfsa') # Would return false as that directory doesn't exist

# To get the size in bytes as an integer for a file use os.path.getsize()
try:
    os.path.getsize('c:\\windows\\example\\file\\calc.exe') # would return the byte size of the file
except:
    print('doesn\'t exist')
# To list out all the files and folders in a directory use os.listdir()
os.listdir('C:\\Users\\georgewolf')


totalSize = 0
for filename in oslistdir('c:\\Intel'):
    if not os.path.isfile(os.path.join('c:\\Intel', filename)):
        continue
    totalSize = totalSize+ os.path.getsize(os.path.join('c:\\Intel', filename))