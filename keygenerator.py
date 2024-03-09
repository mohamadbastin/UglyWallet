### This module either creates a new ethereum key or reads an existing ethereum key from a file.
### The key is used to sign transactions and messages.
### The key is stored in a file called "keyfile" in the same directory as the module.
### this is not safe. It is only for testing purposes. do not use for production. only transfer testnet tokens.

from web3 import Web3
from eth_account import Account


def create_private_key():
    w3 = Web3()
    account = w3.eth.account.create()
    key = w3.to_hex(account.key)
    with open("keyfile.key", "w") as f:
        f.write(key)
    return key, account.address


def get_private_key():
    try:
        with open("keyfile.key", "r") as f:
            print("keyfile found. reading key.")
            key = f.read()
            return key, Account.from_key(key).address
    except FileNotFoundError:
        print("keyfile not found. creating new key.")
        key, address = create_private_key()
        return key, address
