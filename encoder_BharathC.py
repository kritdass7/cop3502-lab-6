# Name: Bharath Chowlur

from encoder_BharathC import encode


def encode(password):
    encoded_password = ""
    for x in password:
        new_digit = (int(x) + 3) % 10
        encoded_password += str(new_digit)
    return encoded_password

def decode(encoded_password):
    pass

