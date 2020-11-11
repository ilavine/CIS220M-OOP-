"""
Program Name:   ScreenCleaner


Writen by:      Iuliia Lavine


Date:           1 November 2020


Synopsis:      This module interacts with the command line and clears the screen
                
"""

import os

def clearScrn(): 
    os.system('cls')
    
def dumpIt(theList):
    for i in range(2, len(theList)):
     print(theList[i])

f0 = open('main_menu.txt', 'r')
theList = f0.readlines()
f0.close()
for i in range(len(theList)):
    theList[i] = theList[i].replace('\n', '')
dumpIt(theList)
x = input('Make a selection: ')
clearScrn()
dumpIt(theList)
x = input('Make a selection: ')