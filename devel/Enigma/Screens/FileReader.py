'''
Project Name:  Final CIS 210 M
Program Name:  FileReader.py
Date:          10 November 2020
Synopsis:      This program converts file into a list
Written by: Iuliia Lavine
       
'''

import Fixer as fx
    
def readFile(fileName):
    fO = open(fileName,"r")
    theList = fO.readlines()
    fO.close()
    theList = fx.fixScrn(theList)
    for i in range(0, 24):
        print(theList[i])
    
   
    return theList   
    
        
