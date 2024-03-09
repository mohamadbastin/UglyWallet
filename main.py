from keygenerator import get_private_key


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

    print("Choose a network:")
    print("1. Goerli Testnet")
    print("2. BSC Testnet")

    print("Connected to network")

    
    # print("choose an option:")
    # print("1. change network")
    # print("2. get balance")
    # print("3. send tokens")
    # print("4. exit")


main()
