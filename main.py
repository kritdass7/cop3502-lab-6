from encoder import encode

encoded_password = None

while True:
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")

    option = int(input("Please enter an option: "))

    if option == 1:
        encoded_password = encode(input("Please enter your password to encode: "))
        print("Your password has been encoded and stored!\n")
    elif option == 2:
        pass
    elif option == 3:
        break
