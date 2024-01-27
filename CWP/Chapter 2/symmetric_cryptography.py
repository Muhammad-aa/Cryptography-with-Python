# Import the necessary libraries.
from cryptography.fernet import Fernet
from colorama import Fore, init

# Initialize colorama
init()

# Generate a key.
key = Fernet.generate_key()

# Creating a Fernet cipher using the  generated key.
cipher_suite = Fernet(key)

# Encrypting a message.
plaintext = b"Message to be Encrypted"
ciphertext = cipher_suite.encrypt(plaintext)

# Display the print results using Magenta and Red for better Visuals.
print(f"{Fore.MAGENTA}Generated Key: {key}")
print(f"{Fore.RED}Encrypted Message: {ciphertext}\n\n")

# Using the same key to create a Fernet cipher (For decryption).
decipher_suite = Fernet(key)

# Decrypting the message.
decrypted_message = decipher_suite.decrypt(ciphertext)

# Printing the decrypted message.
print(f"{Fore.GREEN}Decrypted Message: {decrypted_message.decode()}")
