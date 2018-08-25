def encrypt(string):
    string = [ord(c) for c in string]
    encrypted_string = ""
    for c in string:
        encrypted_string += chr(c + 1)
    return encrypted_string


def decrypt(string):
    string = [ord(c) for c in string]
    decrypted_string = ""
    for c in string:
        decrypted_string += chr(c - 1)
    return decrypted_string
