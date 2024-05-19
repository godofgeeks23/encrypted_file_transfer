# Encrypted File Transfer

Network data-transfer system that uses symmetric encryption for communication.

About Symmetric Encryption:
Symmetric encryption is a type of encryption where only one key (a secret key) is used to both encrypt and decrypt electronic information. The entities communicating via symmetric encryption must exchange the key so that it can be used in the decryption process.


## Usage Instructions

### Server side


On the Server side you run the code as follows:

```$ python3 Server.py <port> [secretkey]```

E.g. ```$ python3 Server.py 4444 password```


### Client side


On the Client side you run the code as follows:

```$ python3 Client.py <command> <filename> <hostname:port> <cipher> [secretkey]```

E.g. ```$ python3 Client.py write 1MB.bin 136.157.19.23:4444 aes128 pass1234 < 1MB.bin```
E.g. ```$ python3 Client.py read 1GB.bin 221.119.52.32:4523 aes256 password > 1GB.bin```


### Command line options


Supported commands:
write   (must pipe the file to write in standard input)
read    (pipe standard output to file you'd like it written to)

### Cipher options:


`none`

`aes128`

`aes256`

Key parameter only used when cipher!=none.

