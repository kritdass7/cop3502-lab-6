# Name: Bharath Chowlur

def decode(encoded_password):
    decoded_password = "" 

    for n in password:
        original = (int(n) - 3) % 10
        decoded_password += str(original)

    return decoded_password
