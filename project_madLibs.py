# Reads text files and lets user add their own text anywhere the words ADJECTIVE, NOUN, VERB or NOUN appears in the text.
# Read the file panda.txt stored on this same folder.
# Path = yourpath
# The results should be printed to the screen and saved to a new text file. (newpanda.txt)

from pathlib import Path
import os, re
import pyinputplus as pyip

# Modify the file panda.txt
panda =  open('C:\\yourpath\panda.txt')
pandaContent = panda.read()
# Transfers the content of panda to newPanda:
newPanda = open('newPanda.txt', 'w')
newPandaWrite = newPanda.write(pandaContent)
# The panda regex:
pandaRegex = re.compile(r'(ADJECTIVE|NOUN|VERB|ANOUN)')
# Getting user input to match in the regex:
while True:
    mo = pandaRegex.search(pandaContent)
    if mo == None:
        break
    elif mo.group() == 'ADJECTIVE':
        print('Enter an adjective: ')
    elif mo.group() == 'NOUN':
        print('Enter a noun: ')
    elif mo.group() == 'VERB':
        print('Enter a verb: ')
    elif mo.group() == 'ANOUN':
        print('Enter another noun: ')
    userInput = input()
    pandaContent = pandaContent.replace(mo.group(), userInput, 1)
# Creating a new panda file and transfering the new content to it:
newPanda = open('newPanda.txt', 'w')
newPanda.write(pandaContent)
# Print the new file content from newpanda.txt:
print(pandaContent)
# Closing everything:
newPanda.close()
panda.close()

