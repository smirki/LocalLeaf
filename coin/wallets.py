class Wallets:
    def __init__(self):
        self.wallets = {}

    def add_wallet(self, wallet):
        self.wallets[wallet.public_key] = wallet

    def get_wallet(self, public_key):
        return self.wallets.get(public_key)

    def has_public_key(self, public_key):
        return public_key in self.wallets

    def __iter__(self):
        return iter(self.wallets.values())
