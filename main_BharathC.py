# Name: Bharath Chowlur

from encoder_BharathC import encode


def main():
    encoded_password = None

    while True:
        print("\nMenu:")
        print("0. Exit")
        print("1. Encode")
        print("2. Decode")

        choice = input("Choose an option: ")

        if choice == "0":
            print("Exiting the program.")
            break
            
        elif choice == "1":
            password = input("Please enter a password: ")
            encoded_password = encode(password)
            print("Encoded password:", encoded_password)

        elif choice == "2":
            pass
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
