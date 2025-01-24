This Python program simulates a simple blockchain with basic functionality like adding blocks, validating the chain, and detecting tampering. 
It implements the Proof-of-Work concept in the mining process for added complexity.

Features:
Block Structure: Each block contains a list of transactions, a timestamp, a previous block’s hash, and its own hash.
Mining: Blocks are mined using a nonce to meet a difficulty condition (Proof-of-Work).
Blockchain: A chain of blocks is maintained, and it is validated for integrity.
Tampering Detection: The program can demonstrate how tampering with the blockchain invalidates it.

Requirements:
Python 3.x (Python 3.6 or higher is recommended).
No external libraries are required as the program only uses built-in Python modules (hashlib, time).



How to Run the Code
1. Clone the Repository (If Applicable)
If you're working with a Git repository, you can clone it to your local machine using the following command:

bash
Copy
git clone <repository_url>
cd <repository_directory>

2. Install Python
Ensure that you have Python installed. You can check by running:

bash
Copy
python --version
If Python is not installed, you can download it from python.org.

3. Run the Code
To run the blockchain simulation, follow these steps:

Open a terminal or command prompt.
Navigate to the directory where the Blockchain.py script is located.
Run the Python script using the following command:
bash
Copy
python Blockchain.py
Expected Output
When the script runs, you should see the following outputs:

A series of blocks printed to the console.
A message validating the blockchain.
A demonstration of how tampering with the blockchain is detected.
Example Output:

bash
Copy
BigBlock 0: [timeStamp: 1632650280.12345, Transactions: ['First Block Transaction'], Previous Hash: 0, Current Hash: <hash_value>]
BigBlock 1: [timeStamp: 1632650285.56789, Transactions: ['Trans1', 'Trans2'], Previous Hash: <previous_hash>, Current Hash: <hash_value>]
BigBlock 2: [timeStamp: 1632650290.87654, Transactions: ['Trans3', 'Trans4'], Previous Hash: <previous_hash>, Current Hash: <hash_value>]

BigBlockchain is valid!
Tampering with block data...
Let's try to change block 1 to Hacked via myBlockchain.chain[1].bigTransactions = ['Hacked']
We change the value of block 1 so tampering will be detected.
BigBlockchain is invalid at block 1

Real quick I'll set block 1 to it's original value
BigBlockchain is valid!
etc.

Code Explanation
1. BigBlock Class
This class represents a block in the blockchain. Each block contains:

bigIndex: The index of the block in the blockchain.
bigTimeStamp: The timestamp when the block was created.
bigTransactions: A list of transactions included in the block.
bigPrevHash: The hash of the previous block.
bigCurrHash: The current hash of the block, calculated after mining.
difficulty: The number of leading zeros the block's hash must have to be considered valid (used for Proof-of-Work).
The mineBlock() method implements the Proof-of-Work algorithm, where it keeps changing the nonce (j) until the hash of the block meets the required difficulty.

2. Blockchain Class
This class manages the blockchain:

createFirstBlock(): Creates the very first block in the chain.
addBlock(): Adds new blocks to the blockchain with new transactions.
validateChain(): Validates the blockchain’s integrity by checking the hashes and links between blocks.
printChain(): Prints out the details of all blocks in the blockchain.
testTamper(): Demonstrates how tampering with block data causes the chain to be invalid.

3. Tampering Simulation
The testTamper() method allows for testing how the blockchain detects tampering. It attempts to modify data within blocks and checks if the blockchain can detect those changes.

Code Walkthrough
Initializing the Blockchain:

The blockchain is initialized by creating the first block with no previous hash.
Blockchain.createFirstBlock() creates the first block using BigBlock, and adds it to the chain.

Adding New Blocks:

The Blockchain.addBlock() method creates a new block using new transactions, attaches it to the chain, and updates the previous block's hash.
Mining a Block:

The mineBlock() method in BigBlock runs a while loop, continuously trying different nonce values to find a hash that meets the difficulty requirement (starts with a number of leading zeros).
The sha256() function from the hashlib module is used to generate the block’s hash.
Blockchain Validation:

The validateChain() method checks the integrity of the blockchain by verifying the hashes between consecutive blocks. If any tampering is detected, it prints an error message.
Demonstrating Tampering:

testTamper() modifies different parts of a block (transactions, index, previous hash, current hash) to show how these changes break the blockchain’s validity.

Optional Enhancements (Bonus)
Proof-of-Work: The mining process can be made more difficult by increasing the difficulty parameter. You can experiment with different difficulty levels to see how it affects the mining process.
Dynamic Transaction Handling: The code can be extended to dynamically add real-time transactions to each block.
