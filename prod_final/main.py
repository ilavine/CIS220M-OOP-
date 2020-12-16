# -*- coding: utf-8 -*-
"""
Program Name:  Enigma.py
Writen by:     Iuliia Lavine
Date:          10 December 2020
Synopsis:      OOP Final Project

"""


import tkinter as tk
from tkinter import *
from PIL import ImageTk,Image
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfilename, asksaveasfile
import invertedPlugBoard
import encode


def open_file(): # tkinter GUI implementation of opening a file
	global text,save_file_id
	open_file_loc=askopenfilename()
	open_file=open(open_file_loc,'r')
	text.delete(1.0,END)
	text.insert(END,open_file.read())
	save_file_id=open_file_loc
    
def save_as_file(): # tkinter GUI implementation of saving a file
	global text2,save_file_id
	name=asksaveasfile(mode='w',defaultextension=".txt")
	text2save=str(text2.get(0.0,END))  
	name.write(text2save)
	name=str(name)[(str(name).find("name='")+6):str(name).find("'",(str(name).find("name='")+6))]
	save_file_id=name 
      
def remove(text): #replaces spaces with < and \n (newlines) with &
    newText=''
    for char in text:
        if char == ' ':
            char = '<'
        elif char == '\n':
            char ='&'
        newText += char
    
    return newText  

def insert(text): #does the opposite of fixEncrypt def
	newText = ""
	for char in text:
		if char == "<":
			char = " "
		elif char == "&":
			char = "\n"
		newText += char
		
	return newText
     
def encryptText(): #prints an encoded text to entry widget 2
      global text
      f = remove(str(text.get(0.0, END)))
      fixText = ' '.join(f[n:n + 6] for n in range(0, len(f), 6))
      fixTextfix = '\n'.join(fixText[n:n + 36] for n in range(0, len(f), 36))
      newText = encode.encode(fixTextfix)
      text2.delete(1.0, END)
      text2.insert(END, newText)

def decryptText(): #prints a decoded text to entry widget 2, reverses spaces and newlines \n
    invertDict = invertedPlugBoard.invPlugBoard()
    textDecrypt = str(text.get(0.0, END))
    stringText = encode.encode(textDecrypt, invertDict)
    f = stringText.replace(' ', '')
    f2 = f.replace('\n', '')
    fixText = insert(f2)
    text2.delete(1.0, END)
    text2.insert(END, fixText)
   
def about(): #provides a text for the helo tab
	filewin = Toplevel(window)
	string = open("info.txt", "r", encoding="UTF8").read()
	button = Label(filewin,text=string)
	button.pack()


# initializes the window
window = tk.Tk()
# customizes the window geometry
window.geometry('760x770')
# customizes the title
window.title("Enigma - CIS220")
window.configure(bg='black')

# initializes the top menu bar
menubar = Menu(window)
helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "About...", command = about)

# imports an image from a file onto the window
my_img = ImageTk.PhotoImage(Image.open("enigma2.png"))

# label widget is used to display an imported image
my_Label = tk.Label(image=my_img, relief="groove")
my_Label.pack(pady=10)

my_Label2 = tk.Label(text = 'Welcome to the Enigma Machine simulator\nPlease enter your text in the widget below or upload a text file', 
                     font=('Verdana',12), relief = 'groove')
my_Label2.pack(pady=10)


# use a command parameter (command = yourfunction) to initialize a function once user presses the button

button1 = tk.Button(window, text="Encryption", command = encryptText, font=('Verdana',12), width=10,  bg='silver')
button2 = tk.Button(window, text="Decryption", command = decryptText, font=('Verdana',12), width=10, bg='silver')
button3 = tk.Button(window, text="Upload txt", font=('Verdana',12), command=open_file, width=10, bg='silver')
button4 = tk.Button(window, text="Save output to a file", command=save_as_file, font=('Verdana',12), bg='silver')
text = ScrolledText(window, font=('Verdana',12), height=5, width=60)
Text = "Enter your message for decryption/encryption or upload a text file" 
text.insert(tk.END, Text)
text2 = ScrolledText(window, font=('Verdana',12), height=5, width=60)
Text2 = "Output text" 
text2.insert(tk.END, Text2)
#text2.configure(state='disabled')
button5 = tk.Button(window, text="Quit", command=window.destroy, font=('Verdana',12), width =10, bg='silver')
my_Label3 = tk.Label(text = 
                     '''If you want to encode the message, press 'Encryption'\n
 If you want to decode the message, press 'Decryption' ''', 
                     font=('Verdana',8), relief = 'groove')
my_Label4 = tk.Label(text = 
                     'Press the button below to save the output to a text file', 
                     font=('Verdana',8), relief = 'groove')

# pushes buttons downward
button3.pack(pady=1)
text.pack(pady=10)
my_Label3.pack(pady=2)
button1.pack(pady=1)
button2.pack(pady=1)
text2.pack(pady=10)
my_Label4.pack(pady=2)
button4.pack(pady=2)
button5.pack(pady=30)


# this ensures that there is a window/menubar
window.config(menu = menubar)
window.mainloop()
