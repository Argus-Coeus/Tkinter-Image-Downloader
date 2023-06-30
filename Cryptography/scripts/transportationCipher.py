#!/usr/bin python3
import math
import sys

def main():
    con = 1

    while(con != 0):
        myMessage = input("Enter Message: ")
        try:
            myKey = int(input("Enter key : "))
        except:
            print("Key must be integer number.")
            sys.exit()

        user = int(input("1. Encrypt \n 2. Decrypt \n [Number] : "))
        if(user == 1):
            #ciphertext
            cipherText =  encryptMessage(myKey, myMessage)
            #print ciphertext
            print(cipherText )
        elif(user == 2):
            plainText =  encryptMessage(myKey, myMessage)
            #print Plaintext
            print(plainText )
        else:
            print("1 -> Encrypt , 2 -> Decrypt.")
        repeat = input("Again [Y|N] : ").lower()
        if (repeat == 'y'):
            con = 1
        elif(repeat == 'n'):
            con = 0       
            print("GOODBYE: Thank you for using us.") 

#the cncryption function to be used
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
    print(''.join(ciphertext))
    return ''.join(ciphertext)

#The decryption function
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
    print(''.join(plaintext))
    return ''.join(plaintext)
    

if __name__=="__main__":
    main()

