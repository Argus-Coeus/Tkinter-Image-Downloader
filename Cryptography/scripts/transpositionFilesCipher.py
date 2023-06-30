#!/usr/bin python3
import time, os, sys
from pylibrary.transposition import Transposition


def main():
    inputFilename = ''
    #Be careful! if a file with the outputfilename name already exists
    #this program will overwrite that file
    outputFilename = ''
    myKey = 10
    myMode = 'encrypt' #set to 'encrypt' or 'decrypt'


    if not os.path.exists(inputFilename):
        print(f'The file {inputFilename} does not exit. Quitting...')
        sys.exit()

    if os.path.exists(outputFilename):
        print(f'This will overwrite the files {outputFilename}. (C)ontinue or (Q)uit?')
        reponse = input('> ')
        if not reponse.lower().startswith('c'):
            sys.exit()

    fileObj = open(inputFilename)
    content = fileObj.read()
    fileObj.close()

    print(f'{myMode.title()}ing')

    startTime = time.time()
    if myMode == 'encrypt':
        translated = Transposition.encryptMessage(myKey,content)
    elif myMode == 'decrypt':
        translated  = Transposition.decryptMessage(myKey,content)
    totalTime = round(time.time() - startTime,2)
    print(f'{myMode.title()}ion time: {totalTime} seconds.')


    outputFileObj = open(outputFilename,'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print(f'Done {myMode} {inputFilename} ({len(content)}).')
    print(f'{myMode.title()}ed file is {outputFilename}.')



if __name__=='__main__':
    main()