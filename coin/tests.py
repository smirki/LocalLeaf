import requests

resp = requests.get('http://localhost:5000/create_wallet?initial_balance=100')
wallet1_private_key = resp.json()['private_key']
wallet1_public_key = resp.json()['public_key']
wallet1_balance = resp.json()['balance']

resp = requests.get('http://localhost:5000/create_wallet?initial_balance=0')
wallet2_public_key = resp.json()['public_key']
wallet2_balance = resp.json()['balance']

data = {
    'private_key': wallet1_private_key,
    'recipient': wallet2_public_key,
    'amount': 10
}
resp = requests.post('http://localhost:5000/send_transaction', params=data)

if resp.status_code == 201:
    print("Transaction sent successfully!")
else:
    print("Transaction failed.")

resp = requests.get(f'http://localhost:5000/get_balance?address={wallet1_public_key}')
wallet1_balance = resp.json()['balance']
resp = requests.get(f'http://localhost:5000/get_balance?address={wallet2_public_key}')
wallet2_balance = resp.json()['balance']
print(f"Wallet1 balance: {wallet1_balance}")
print(f"Wallet2 balance: {wallet2_balance}")

resp = requests.post(f'http://localhost:5000/mine?miner_address={wallet1_public_key}')
if resp.status_code == 200:
    block = resp.json()
    print(f"Block mined successfully! Block mined for {wallet1_public_key}")
else:
    print("Block mining failed.")

resp = requests.get('http://localhost:5000/chain')
chain_length = resp.json()['length']
print(f"Chain length: {chain_length}")

resp = requests.get('http://localhost:5000/create_wallet?initial_balance=0')
wallet3_public_key = resp.json()['public_key']

data = {
    'private_key': wallet1_private_key,
    'recipient': wallet3_public_key,
    'amount': 5
}
resp = requests.post('http://localhost:5000/send_transaction', params=data)

if resp.status_code == 201:
    print("Transaction sent successfully!")
else:
    print("Transaction failed.")

resp = requests.get(f'http://localhost:5000/get_balance?address={wallet2_public_key}')
wallet2_balance = resp.json()['balance']
resp = requests.get(f'http://localhost:5000/get_balance?address={wallet3_public_key}')
wallet3_balance = resp.json()['balance']
print(f"Wallet2 balance: {wallet2_balance}")
print(f"Wallet3 balance: {wallet3_balance}")

# Test the new API endpoints
block_index = 1
resp = requests.get(f'http://localhost:5000/get_block_info?index={block_index}')
if resp.status_code == 200:
    block_info = resp.json()
    print(f"Block info for index {block_index}: {block_info}")
else:
    print("Failed to get block info.")

resp = requests.get(f'http://localhost:5000/get_market_cap')
if resp.status_code == 200:
    market_cap = resp.json()['market_cap']
    print(f"Market cap: {market_cap}")
else:
    print("Failed to get market cap.")
