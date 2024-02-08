from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os


def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key


def save_key_to_file(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)


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
