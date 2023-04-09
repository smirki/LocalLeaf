import hashlib
import json
import ecdsa

class Wallet:
    def __init__(self, initial_balance=0):
        self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.public_key = self.private_key.get_verifying_key().to_string().hex()
        self.balance = initial_balance

    def add_balance(self, amount):
        self.balance += amount
    
    def subtract_balance(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self, address):
        if address == self.public_key:
            return self.balance
        else:
            return 0

    def create_transaction(self, recipient_address, amount):
        if self.balance < amount:
            print("Error: Not enough balance")
            return None

        transaction = {"sender": self.public_key, "recipient": recipient_address, "amount": amount}

        message = json.dumps(transaction).encode()
        signature = self.private_key.sign(message).hex()

        transaction["signature"] = signature

        self.balance -= amount

        return transaction
