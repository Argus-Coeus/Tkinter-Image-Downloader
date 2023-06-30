#!/usr/bin python3
#Reverse Cipher
"""Storing Objects"""
message =  "Somethinh"
translated = ""

"""Main Operation"""
i = len(message) - 1
while i >= 0: 
    translated = translated + message[i]
    i = i -1

"""Print Output"""
print(translated)
