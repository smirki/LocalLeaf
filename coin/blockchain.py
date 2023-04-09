import time
from block import *
from wallet import *
from ecdsa import VerifyingKey, BadSignatureError
from wallets import *
import json
import binascii

BLOCK_REWARD = 1

class Blockchain:
    def __init__(self, wallets):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.wallets = wallets
        self.wallet = Wallet()
        self.total_supply = 0

    def create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.block_hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]
    
    difficulty = 2
    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        previous_hash = self.last_block.block_hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        block.block_hash = proof
        self.chain.append(block)
        return True
    
    def is_valid_proof(self, block, block_hash):
        return (block_hash.startswith('0' * Blockchain.difficulty) and block_hash == block.compute_hash())
    
    def add_new_transaction(self, sender, recipient, amount, signature):
        # Check if sender and recipient exist in wallets
        sender_wallet = self.wallets.get_wallet(sender)
        recipient_wallet = self.wallets.get_wallet(recipient)
        if not sender_wallet or not recipient_wallet:
            return False

        # Verify the transaction signature
        try:
            public_key = VerifyingKey.from_string(bytes.fromhex(sender), curve=ecdsa.SECP256k1)
            if not public_key.verify(binascii.unhexlify(signature), json.dumps({"sender": sender, "recipient": recipient, "amount": amount}).encode()):
                return False
        except BadSignatureError:
            return False

        # Check if amount is valid and greater than zero
        if amount <= 0:
            return False

        # Add the transaction to the unconfirmed transactions list
        transaction = {"sender": sender, "recipient": recipient, "amount": amount, "signature": signature}
        self.unconfirmed_transactions.append(transaction)

        # Update sender's and recipient's balances
        # sender_wallet.subtract_balance(amount)
        recipient_wallet.add_balance(amount)

        return True

    def get_block_info(self, index):
        if index >= len(self.chain):
            return None

        block = self.chain[index]
        return {
            "index": block.index,
            "transactions": block.transactions,
            "timestamp": block.timestamp,
            "previous_hash": block.previous_hash,
            "hash": block.block_hash,
            "nonce": block.nonce
        }

    def get_market_cap(self):
        return self.total_supply

    def mine(self, miner):
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block
        new_block = Block(index=last_block.index + 1, transactions=self.unconfirmed_transactions, timestamp=time.time(), previous_hash=last_block.block_hash)
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)

        # Update the total supply and miner's balance
        self.total_supply += BLOCK_REWARD
        self.wallets.get_wallet(miner).add_balance(BLOCK_REWARD)

        self.unconfirmed_transactions = []
        return new_block.index
    
    def get_balance(self, address):
        balance = self.wallet.get_balance(address)
        return balance