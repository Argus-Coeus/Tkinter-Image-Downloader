#!/usr/bin python3 
#The message to be decrypted 
message = "@iH<,{|jbRH?L^VjGJH<vn3p7I,x~@1jyt>x?,!YAJr*08P"

#Characters for the encryptions
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Looping into the keys 
for key in range(len(LETTERS)):

    #The decoded message
    translated = ''


    #Looping into the message
    for symbol in message:
        #Checking  if the characters in the message is in the letters
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            num = num - key
            #Checking if num is greater than 0
            if num < 0:
                num = num + len(LETTERS)

            #appending the character to the translated
            translated = translated + LETTERS[num]

        else:
            #Adding the characters in the message to the translated
            translated = translated + symbol
    #displaying the number of keys and the message decoded
    print(f"key: {key} : {translated}")
