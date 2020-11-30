'''
Project Name:  Final CIS 210 M
Program Name:  Fixer.py
Date:          10 November 2020
Synopsis:      This program removes the carriage return line and replaces with a line feed
Written by:    Iuliia Lavine
       
'''

def fixScrn(theList):
    for i in range(len(theList)):
        theList[i] = theList[i].replace('\n', '')
    return theList
