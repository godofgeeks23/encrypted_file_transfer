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

if __name__ == "__main__":
    # Generate key pair for server
    server_private_key, server_public_key = generate_key_pair()
    save_key_to_file(server_private_key, 'server_private_key.pem')
    save_key_to_file(server_public_key, 'server_public_key.pem')
