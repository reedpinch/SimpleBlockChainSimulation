#Imports for hashing and timestamps
import hashlib
import time

#Make blockchain class
#This class is unused by the rest of the program but is here to show progress was made. 
#class Block:
    #set fields
    #def __init__(self, index, timeStamp, transactions, prevHash):
    #    self.index = index
    #    self.timeStamp = timeStamp
    #    self.transactions = transactions
    #    self.prevHash = prevHash
    #    self.currHash = self.calculateHash()
    #encrypt with a new hash
    #def calculateHash(self):
    #   blockString =  f"{self.index}{self.timeStamp}{self.transactions}{self.prevHash}"
    #    return hashlib.sha256(blockString.encode('utf-8')).hexdigest()
    
    #def __str__(self):
    #   return f"Block {self.index}: [timeStamp: {self.timeStamp}, Transactions: {self.transactions}, Previous Hash: {self.prevHash}, Current Hash: {self.currHash}]"
    
#Make a BigBlock class for the optional bonus
class BigBlock:
    #Set fields
    def __init__(self, bigIndex, bigTimeStamp, bigTransactions, bigPrevHash, difficulty=4):
        self.bigIndex = bigIndex
        self.bigTimeStamp = bigTimeStamp
        self.bigTransactions = bigTransactions
        self.bigPrevHash = bigPrevHash
        self.difficulty = difficulty
        self.bigCurrHash = self.mineBlock()  # The block's hash is computed

    def mineBlock(self):
        j = 0 #Initialize the number used once
        while True: #Start an infinite loop that will try different values for j
            #Create a string of the block's data
            bigBlockString = f"{self.bigIndex}{self.bigTimeStamp}{self.bigTransactions}{self.bigPrevHash}{j}"
            #Hash the block string using SHA-256 and get the hexadecimal representation
            bigBlockHash = hashlib.sha256(bigBlockString.encode('utf-8')).hexdigest()
            #Check if the hash starts with the required number of zeros
            if bigBlockHash[:self.difficulty] == '0' * self.difficulty:
                return bigBlockHash
            j += 1
    #Print each block
    def __str__(self):
        return f"BigBlock {self.bigIndex}: [timeStamp: {self.bigTimeStamp}, Transactions: {self.bigTransactions}, Previous Hash: {self.bigPrevHash}, Current Hash: {self.bigCurrHash}]"

class Blockchain:
    #initialize the chain
    def __init__(self):
        self.chain = []
	#create the first block from which we will seed all other blocks
        self.createFirstBlock()
        
    #Create the first block
    def createFirstBlock(self):
        # First block has no previous block, so its prevHash is set to 0
        firstBlock = BigBlock(0, time.time(), ["First Block Transaction"], "0")
        #the below attaches our first block to the chain array
        self.chain.append(firstBlock)
        
    #Add a new block
    def addBlock(self, transactions):
        #grab the block at the end of the chain
        prevBlock = self.chain[-1]
        #increment index
        newIndex = prevBlock.bigIndex + 1
        #give it a timeStamp
        timeStamp = time.time()
        #create the new block
        newBlock = BigBlock(newIndex, timeStamp, transactions, prevBlock.bigCurrHash)
        #add our new block to the chain array
        self.chain.append(newBlock)
        
    #Validate the blockchain
    def validateChain(self):
        for i in range(1, len(self.chain)):
            bigPrevBlock = self.chain[i - 1]
            bigCurrBlock = self.chain[i]
            # Check if the current block's previous hash matches the previous block's hash
            if bigCurrBlock.bigPrevHash != bigPrevBlock.bigCurrHash:
                print(f"BigBlockchain is invalid at block {bigCurrBlock.bigIndex}")
                return False
            # Check if the current block's hash is correct
            if bigCurrBlock.bigCurrHash != bigCurrBlock.mineBlock():
                print(f"BigBlockchain is invalid at block {bigCurrBlock.bigIndex}")
                return False
        print("BigBlockchain is valid!")
        return True

    #Print the blockchain
    def printChain(self):
        for block in self.chain:
            print(block)

    #Helper Method for running tests
    def testTamper(self):
        print("\nTampering with block data...")
        print("Let's try to change block 1 to Hacked via myBlockchain.chain[1].bigTransactions = ['Hacked']")
        temp2 = myBlockchain.chain[1].bigTransactions
        myBlockchain.chain[1].bigTransactions = ["Hacked"]
        print("\nWe change the value of block 1 so tampering will be detected.")
        myBlockchain.validateChain()  # Should detect tampering
        print("\nReal quick I'll set block 1 to it's original value")
        myBlockchain.chain[1].bigTransactions = temp2
        myBlockchain.validateChain()  # Should detect tampering
    
        print("\nNow we'll mess with the index via myBlockchain.chain[1].bigIndex = 7")
        temp3 = myBlockchain.chain[1].bigIndex
        myBlockchain.chain[1].bigIndex = 7
        myBlockchain.validateChain()  # Should detect tampering
        print("\nReal quick I'll set block 1 index to it's original value")
        myBlockchain.chain[1].bigIndex = temp3
        myBlockchain.validateChain()  # Should detect tampering
    
        print("\nNow let's change the previous hash via myBlockchain.chain[1].bigPrevHash = 'abcdefg1234567'")
        temp = myBlockchain.chain[1].bigPrevHash
        myBlockchain.chain[1].bigPrevHash = "abcdefg1234567"
        myBlockchain.validateChain()  # Should detect tampering
        print("\nReal quick I'll set block 1 to it's original bigPrevHash")
        myBlockchain.chain[1].bigPrevHash = temp
        myBlockchain.validateChain()  # Should detect tampering
    
        print("\nFinally let's change the current hash value via myBlockchain.chain[1].bigCurrHash = '1234567abcdefg'") 
        temp1 = myBlockchain.chain[1].bigCurrHash
        myBlockchain.chain[1].bigCurrHash = "1234567abcdefg"      
        myBlockchain.validateChain()  # Should detect tampering
        print("\nReal quick I'll set block 1 to it's original currHash")
        myBlockchain.chain[1].bigCurrHash = temp1
        myBlockchain.validateChain()  # Should detect tampering
        
            
#Main method
if __name__ == "__main__":
    # make a new blockchain
    myBlockchain = Blockchain()

    # Add some blocks to the blockchain
    myBlockchain.addBlock(["Wow Reed", "This is Great"])
    myBlockchain.addBlock(["I think", "We'll offer you the position"])

    # Print the blockchain
    myBlockchain.printChain()

    # Validate the blockchain
    myBlockchain.validateChain()

    # Demonstrate tampering
    myBlockchain.testTamper()
    




















    
