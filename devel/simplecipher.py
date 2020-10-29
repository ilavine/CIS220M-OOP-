# -*- coding: utf-8 -*-
"""

Program Name:   Basic Cipher


Writen by:      Iuliia Lavine


Date:           20 October 2020


Synopsis:      This is a basic cipher that shifts letters by the specified number
                
"""

# imports

import collections
import string

# here we get upper and lower letters 

upper_letters = collections.deque(string.ascii_uppercase)
lower_letters = collections.deque(string.ascii_lowercase)

# gets a list of letters and converts to a string 

upper = ''.join(list(upper_letters))
lower = ''.join(list(lower_letters))


def encrypt(n, s): # encryption function performs the positive shift
    
   encryptedMessage = '' 
   
   for c in s: # finds characters in the message 
        if c.islower(): # and determines whether the character is upper or lowercase
        # calculates the position of the character and performs the positive shift by the specified value
        #finds the character at the new position 
            if c in lower: encryptedMessage += lower[(lower.index(c) + n) % len(lower)]
        elif c.isupper():
            # this is used to replace the capital letters by the new characters
            if c in upper: encryptedMessage += upper[(upper.index(c) + n) % len(upper)]
        else: encryptedMessage += c
   
   print('Encrypted text: ', encryptedMessage) #prints the encrypted message
   return encryptedMessage

def decrypt(n, s): # decryption function performs the negative shift
    
    decryptedMessage = '' 
    
    for c in s: #
        if c.islower():
            if c in lower: decryptedMessage += lower[(lower.index(c) - n) % len(lower)]
        elif c.isupper():
            if c in upper: decryptedMessage += upper[(upper.index(c) - n) % len(upper)]
        else: decryptedMessage += c
        
    print('Decrypted text: ', decryptedMessage)    
    return decryptedMessage
    


class main:
    # asks whether a user wants to encrypt or decrypt a message
    choice = input("This a simple cipher. Would you like to encrypt a message or decrypt a message? (e or d): ")
    if(choice == "e"):
        s = input("Enter message to encrypt: ") # enters the message
        n = int(input("Enter the key (this will determine by how many letters the text will be shifted): ")) #enters the key value
        encrypt(n, s)
    elif(choice == "d"):
        s = input("Enter message to decrypt: ") # enters the message
        n= int(input("Enter the key: ")) # enters the key value
        decrypt(n, s)