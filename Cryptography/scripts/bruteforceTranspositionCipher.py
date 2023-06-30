#!/usr/bin python3
#Transposition BruteForce Cipher 
from pylibrary.transposition import Transposition
import random,sys


def main():
    random.seed(42)
    
    for i in range(20):

        message  = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randint(4,40)
        
        message = list(message)
        random.shuffle(message)
        message = ''.join(message)

        print(f'Test #{i+1}: {message[:50]}')

        for key in range(1, len(message)):
            encrypted = Transposition.encryptMessage(key,message)
            decrypted = Transposition.decryptMessage(key,message)

            if message != decrypted:
                print(f'Mismatch with key {key} and message {message}')
                print(decrypted)
                sys.exit()

    print('Transposition Cipher test passed.')



if __name__ == '__main__':
    main()
