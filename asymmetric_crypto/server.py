# use this for decryption

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


if __name__ == "__main__":

    with open('encrypted_file.bin', 'rb') as f:
        encrypted_data = f.read()

    server_private_key = load_key_from_file('server_private_key.pem')

    decrypted_data = decrypt_file(encrypted_data, server_private_key)
    with open('decrypted_file.txt', 'wb') as f:
        f.write(decrypted_data)
