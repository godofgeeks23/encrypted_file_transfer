# use this for encryption

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os


def load_key_from_file(filename):
    with open(filename, 'rb') as f:
        key = f.read()
    return key


def encrypt_file(file_path, public_key):
    with open(file_path, 'rb') as f:
        data = f.read()

    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    encrypted_data = cipher.encrypt(data)
    return encrypted_data


def decrypt_file(encrypted_data, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    decrypted_data = cipher.decrypt(encrypted_data)
    return decrypted_data


# Example usage
if __name__ == "__main__":
    server_public_key = load_key_from_file('server_public_key.pem')

    encrypted_data = encrypt_file('file_to_encrypt.txt', server_public_key)

    with open('encrypted_file.bin', 'wb') as f:
        f.write(encrypted_data)
