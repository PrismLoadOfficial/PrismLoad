# Founded by Zohrab Aliyev and Rían Ó Donnell **2021**

# Using Python and maybe more...
# Coding: utf-8

#-----Json Usage Plan
#imports
#import json
#from time import time

#-----End of json time

# Codes for Defining the blockchain
from hashlib import sha256

def updatehash(*args):
    hashing_text =""; h = sha256()
    for arg in args:
        hashing_text += str(arg)

    h.update(hashing_text.encode('utf-8'))
    return h.hexdigest()

class Block():



    def __init__(self,number=0, previous_hash="0"*64, data=None, nonce=0):
        self.data = data
        self.number = number
        self.previous_hash = previous_hash
        self.nonce = nonce

    def hash(self):
        return updatehash(
            self.previous_hash,
            self.number,
            self.data,
            self.nonce
        )

    def __str__(self):
        return str("Block#: %s\nHash: %s\nPrevious: %s\nData: %s\nNonce: %s\n" %(self.number, self.hash(), self.previous_hash, self.data, self.nonce))
#--- for main() info, Off = No info, On = add info


class Blockchain():
    difficulty = 5 #only change in case of error note: change to million if u are tony stark; Rian note: POGGERS


    def __init__(self):
        self.chain = []

    def add(self, block):
        self.chain.append(block)

    def remove(self, block):
        self.chain.remove(block)

    #mining function
    def mine(self, block):
        try:
            block.previous_hash = self.chain[-1].hash()
        #ignore IndexError
        except IndexError:
            pass

        #Search infinitly
        while True:
            if block.hash()[:self.difficulty] == "0" * self.difficulty:
                self.add(block); break
            else:
                block.nonce += 1

    def isValid(self): #check if the block is valid
        for i in range(1, len(self.chain)):
            _previous = self.chain[i].previous_hash
            _current = self.chain[i-1].hash()
            if _previous != _current or _current[:self.difficulty] != "0"*self.difficulty:
                return False
        return True





def main():

    blockchain = Blockchain()
    #database string
    database = ["Test", "Test2", "Test3", "Test4"]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))
#print chain with out all the unnessary prints
    print(r""" ___     _          _                 _
| _ \_ _(_)____ __ | |   ___  __ _ __| |
|  _/ '_| (_-< '  \| |__/ _ \/ _` / _` |
|_| |_| |_/__/_|_|_|____\___/\__,_\__,_|
                                             """)
    print("Created by Rían Ó Donnell and Zohrab Aliyev")
    print("\n")
    print(blockchain.chain)
    for block in blockchain.chain:
        print(block)


    print(blockchain.isValid())




    #print(block) #-remove from highlight to see logs.

if __name__ == '__main__':
    main()
