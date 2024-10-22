# Name: Krit Dass


def encode(password):
    encoded_password = ""

    for n in password:
        n = int(n)
        n += 3
        n %= 10

        encoded_password += str(n)

    return encoded_password

