
"""
Program Name:  invertPlugBoard.py
Writen by:     Iuliia Lavine
Date:          11 December 2020
Synopsis:      This program reverse/inverts a dictionary mapping.

Code Source: https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
     
"""

plugBoard = {
        '<': 'C',
        '!': 'j',
        '"': 'z',
        '(': 'k',
        ')': 's',
        '.': 'l',
        '0': 'T',
        '1': 'N',
        '2': 'Z',
        '3': 'R',
        '4': 'u',
        '5': 'M',
        '6': 'K',
        '7': 'Q',
        '8': 'E',
        '9': 'f',
        '?': 'B',
        'A': 'g',
        'B': 'H',
        'C': 'X',
        'D': 'A',
        'E': 'a',
        'F': 'x',
        'G': 'p',
        'H': 'D',
        'I': 'q',
        'J': 'm',
        'K': '.',
        'L': 'i',
        'M': 't',
        'N': '(',
        'O': 'd',
        'P': 'L',
        'Q': ')',
        'R': 'w',
        'S': 'y',
        'T': 'o',
        'U': '!',
        'V': '5',
        'W': 'e',
        'X': 'S',
        'Y': '<',
        'Z': 'b',
        'a': '2',
        'b': 'W',
        'c': ',',
        'd': 'P',
        'e': 'V',
        'f': '„',
        'g': '0',
        'h': 'F',
        'i': '9',
        'j': 'v',
        'k': '8',
        'l': 'Y',
        'm': 'G',
        'n': '7',
        'o': 'r',
        'p': 'n',
        'q': '1',
        'r': 'J',
        's': 'I',
        't': 'O',
        'u': 'h',
        'v': 'c',
        'w': '6',
        'x': '4',
        'y': '?',
        'z': 'U',
        ',': '3',
        '„': '"'
    }

def invPlugBoard():
    
    inv_map = {v: k for k, v in plugBoard.items()}

    return inv_map
