#!/usr/bin python3 
"""Message to be encrypted or Decrypted."""
message = "GUVF VF ZL FRPERG ZRFFNTR"
key = 13 #The number can be changed to any number you want.
mode = "decrypt" #Can be changed to encrypt or decrypt.

"""This the letter and symbols that help in the encryption and decryption."""
SPECIAL = '!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`a bcdefghijklmnopqrstuvwxyz{|}~'
NORMAL = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Choose between the normal or special
LETTERS = SPECIAL

translated = ""  # The encrypted or decrypted message will be stored here.
message = message.upper()

"""Main Operation of the Cryptography"""
for symbol in message:
    if symbol in LETTERS:
        num = LETTERS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)
                            
        translated = translated + LETTERS[num]
    else:
        translated = translated + symbol

print(translated)
print(mode)
