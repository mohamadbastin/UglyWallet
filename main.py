from keygenerator import get_private_key
import web3


def main():
    print("UGLY WALLET")
    print("getting private key...")
    key, address = get_private_key()
    if key is None or address is None:
        print("could not get private key. exiting.")
        return
    print("private key:", key)

    print("-------" * 5)

    print("wallet: ", address)

    # print("Choose a network:")
    # print("1. Goerli Testnet")
    # print("2. BSC Testnet")

    w3 = web3.Web3(web3.HTTPProvider("https://rpc.ankr.com/eth_goerli"))

    if not w3.is_connected():
        print("Could not connect to Goerli Testnet network. Exiting.")
        return
    print("Connected to Goerli Testnet network")

    print("choose an option:")
    # print("1. change network")
    print("2. get balance")
    print("3. send tokens")
    # print("4. exit")

    option = input("option: ")

    if option == "2":
        print("getting balance...")
        balance = w3.eth.get_balance(address)
        print(f"balance: {w3.from_wei(balance, 'ether')} ETH")

    elif option == "3":
        # print("enter address:")
        to_address = "0xFd7716d8B0786349C6515C3aDBadD12a093E6574"
        # print("enter amount:")
        amount = 0.01
        print("sending...")
        tx = {
            "chainId": 5,
            "from": address,
            "to": to_address,
            "value": w3.to_wei(amount, "ether"),
            "nonce": w3.eth.get_transaction_count(address),
            "gas": 200000,
            "maxFeePerGas": 2000000000,
            "maxPriorityFeePerGas": 1000000000,
        }

        signed_tx = w3.eth.account.sign_transaction(tx, key)

        tx_hash = w3.eth.send_raw_transaction(signed_tx.rawTransaction)

        transaction = w3.eth.wait_for_transaction_receipt(tx_hash)

        print("transaction sent. hash:", tx_hash.hex())
        print("transaction:", transaction)


main()
