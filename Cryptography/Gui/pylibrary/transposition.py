#!/usr/bin python
import math

class Transposition(object):
    def __init__(self):
        var = None
    
    def encryptMessage(key,message):
        ciphertext = [''] * key
        #Looping the columns
        for col in range(key):
            pointer = col
            #Looping to check the if the size of the message is less than the pointer
            while pointer < len(message):
                #stores it into the ciphertext by indexing
                ciphertext[col] += message[pointer]
                #Incresing the pointer in each iteration
                pointer += key
        #Return the ciphertext
        return ''.join(ciphertext)

    def decryptMessage(key,message):
        #finding the ceiliing number of the message divided by the key 
        numOfColumns  = math.ceil(len(message)/key)
        # Storing the key inside the number of col
        numOfRows  = key
        #Finding the number of shadow boxes in the plaintext
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        #Arrange in the plaintext
        plaintext = [''] * numOfColumns
        #Col and Row
        col = 0 
        row = 0
        #Looping in the message
        for symbol in message:
            plaintext[col] += symbol

            #Arranging the ciphertext to it's normal plaintext
            if (col == numOfColumns) or (col == numOfColumns -1 and
                                        row >= numOfRows - numOfShadedBoxes):
                col = 0
                row += 1
        return ''.join(plaintext)
    def __str__(self) -> str:
        return "More funcitons will be added soon"

