# Asymmetric File Encryption

## Usage -

### Pre-requisites

Install pycryptodome library using pip:

```$ pip install pycryptodome```

### Steps

Step 1: Run the code on both devices to generate key pairs. Save the keys in files:

```
# Server device
server_private_key, server_public_key = generate_key_pair()
save_key_to_file(server_private_key, 'server_private_key.pem')
save_key_to_file(server_public_key, 'server_public_key.pem')
```

```
# Client device
client_private_key, client_public_key = generate_key_pair()
save_key_to_file(client_private_key, 'client_private_key.pem')
save_key_to_file(client_public_key, 'client_public_key.pem')
```

Step 2: Transfer the public keys between the devices securely. You can use secure channels like SSH, HTTPS, or manually transfer the keys using a USB drive.

Step 3: On the client device, encrypt a file using the server's public key:

```
client_public_key = load_key_from_file('client_public_key.pem')
encrypted_data = encrypt_file('file_to_encrypt.txt', client_public_key)
with open('encrypted_file.bin', 'wb') as f:
    f.write(encrypted_data)

```

Step 4: Transfer the encrypted file ('encrypted_file.bin') to the server device using a secure channel.

Step 5: On the server device, decrypt the encrypted file using the server's private key:

```
server_private_key = load_key_from_file('server_private_key.pem')
with open('encrypted_file.bin', 'rb') as f:
    encrypted_data = f.read()
decrypted_data = decrypt_file(encrypted_data, server_private_key)
with open('decrypted_file.txt', 'wb') as f:
    f.write(decrypted_data)
```

After completing these steps, the file ('file_to_encrypt.txt') is securely transferred from the client device to the server device. It's encrypted during transit using the server's public key and can only be decrypted by the server using its private key.





