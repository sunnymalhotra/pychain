import hashlib
import datetime
import json


# Part 1: Creating a Blockchain
class Blockchain:

    def __init__(self):
        """
        Initialize Blockchain and create Genesis block
        """
        self.chain = []

        # create genesis block ie first block of blockchain
        # each blockchain will have it's own proof, a common practise is to start with 1
        # for genesis block, common practise is to use previous_hash '0'
        self.create_block(proof=1, previous_hash='0')

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': datetime.datetime.now(),
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1

        return new_proof
    
# Part 2: Mining our Blockchain

