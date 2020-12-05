'''
Project Name:  Enigma Project
Program Name:  Driver_v2.0.py
Date:          10 November 2020
Synopsis:      This is a driver program
Written by:    Iuliia lavine
'''
import Setup as sp
import FileReader as fr
import os 
import sys

fr.readFile(sp.getWelcome())

    
class Menu:
    #Display a menu and respond to choices when run
    def __init__(self):
        
        self.choices = {
                "W": self.welcome,
                "Y": self.main_menu,
                "D": self.decrypter,
                "E": self.encrypter,
                "I": self.info
                }
        
    def display(self): #this line will always display at the bottom of each screen
        print("""
Press Y To Proceed To Main Menu \n
Press Z To Exit The Application       
""")

        

    def run(self):
        
        #Display the menu and respond to choices
        while True:
            self.display()
            choice = input("Make a selection: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
                
    def welcome(self):
        os.system('cls')
        return fr.readFile(sp.getWelcome())

    def main_menu(self):
        os.system('cls')   
        return fr.readFile(sp.getMainMenu())
        
         
    def decrypter(self):
        os.system('cls')
        return fr.readFile(sp.getDecrypter())

    def encrypter(self):
        os.system('cls')
        return fr.readFile(sp.getEncrypter())
        
    def info(self):
        os.system('cls')
        return fr.readFile(sp.getInfo())
        
    def exit(self):
        print("Thank you and see you again soon!")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()
