from flask import Flask, request, jsonify
import requests
from blockchain import *
from wallet import Wallet
from wallets import *

app = Flask(__name__)

wallets = Wallets()
blockchain = Blockchain(wallets)


@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({"length": len(chain_data),
                    "chain": chain_data})

@app.route('/mine', methods=['POST'])
def mine_blocks():
    miner_address = request.args.get('miner_address')
    blockchain.mine(miner_address)
    chain_data = []

    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return jsonify({"length": len(chain_data),
                    "chain": chain_data})

@app.route('/get_balance', methods=['GET'])
def get_balance():
    address = request.args.get('address')
    wallet = wallets.get_wallet(address)
    if wallet is not None:
        balance = wallet.balance
        return jsonify({"balance": balance})
    else:
        return "wallet not found", 404

@app.route('/create_wallet', methods=['GET'])
def create_wallet():
    print("hi")
    initial_balance = request.args.get('initial_balance', default=0, type=int)
    wallet = Wallet(initial_balance=initial_balance)
    wallets.add_wallet(wallet)
    response = {
        'private_key': wallet.private_key.to_string().hex(),
        'public_key': wallet.public_key,
        'balance': wallet.balance
    }
    return json.dumps(response)

@app.route('/send_transaction', methods=['POST'])
def send_transaction():
    sender_private_key = request.args.get('private_key')
    recipient_address = request.args.get('recipient')
    amount = float(request.args.get('amount'))

    sk = ecdsa.SigningKey.from_string(bytes.fromhex(sender_private_key), curve=ecdsa.SECP256k1)
    sender_public_key = sk.get_verifying_key().to_string().hex()

    if not wallets.has_public_key(sender_public_key):
        return "wallet not found", 404

    wallet = wallets.get_wallet(sender_public_key)
    transaction = wallet.create_transaction(recipient_address, amount)

    if transaction is None:
        return "failed", 500

    if blockchain.add_new_transaction(sender_public_key, recipient_address, amount, transaction['signature']):
        return "success", 201
    else:
        return "failed", 500

@app.route('/get_block_info', methods=['GET'])
def get_block_info():
    index = request.args.get('index', type=int)
    block_info = blockchain.get_block_info(index)
    if block_info is not None:
        return jsonify(block_info)
    else:
        return "block not found", 404

@app.route('/get_market_cap', methods=['GET'])
def get_market_cap():
    market_cap = blockchain.get_market_cap()
    return jsonify({"market_cap": market_cap})


app.run(debug=True, port=5000)