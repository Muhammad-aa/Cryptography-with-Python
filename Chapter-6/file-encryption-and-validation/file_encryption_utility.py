# Import necessary libraries.
import sys
from cryptography.fernet import Fernet
from colorama import Fore, init

# Initialize colorama for colored output in the terminal.
init()


# Function to generate a new encryption/decryption key.
def generate_key():
    return Fernet.generate_key()


# Function to save a key to a file.
def save_key(key, filename="secret_key.key"):
    with open(filename, "wb") as key_file:
        key_file.write(key)


# Function to load a key from a file.
def load_key(filename="secret_key.key"):
    return open(filename, "rb").read()


# Function to encrypt a file.
def encrypt_file(key, input_file):
    # Create a Fernet cipher with the provided key
    cipher = Fernet(key)

    # Read the plaintext from the input file.
    with open(input_file, "rb") as file:
        plaintext = file.read()

    # Encrypt the plaintext
    encrypted_data = cipher.encrypt(plaintext)

    # Overwrite the input file with the encrypted data.
    with open(input_file, "wb") as file:
        file.write(encrypted_data)


# Function to decrypt a file.
def decrypt_file(key, input_file):
    # Create a Fernet cipher with the provided key.
    cipher = Fernet(key)

    # Read the encrypted data from the input file.
    with open(input_file, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = cipher.decrypt(encrypted_data)

    # Overwrite the input file with the decrypted data
    with open(input_file, "wb") as file:
        file.write(decrypted_data)


# Get user input to choose between encryption and decryption.
user_input = input(
    '[?] Do you want to encrypt or decrypt a file?\n\nSelect option 1 for encryption and 2 for decryption: ')

# Encryption process.
if user_input == '1':
    try:
        # Get input file and key from the user
        file_to_encrypt = input("Enter the path to the input file: ")

        # Generate a new key and save it to a file
        key = generate_key()
        save_key(key)

        # Encrypt the input file using the generated key
        encrypt_file(key, file_to_encrypt)

    except Exception:
        # Handle exceptions and print an error message
        print(f'{Fore.RED}[+] Please make sure to specify a valid file.')

    else:
        # Print a success message if encryption is successful
        print(f'{Fore.GREEN}[+] {file_to_encrypt} Encrypted Successfully.')


# Decryption process.
elif user_input == '2':
    try:
        # Get input file and key from the user
        input_to_decrypt = input("Enter the path to the input file: ")

        # Load the key from a file for decryption
        loaded_key = load_key()

        # Decrypt the input file using the loaded key
        decrypt_file(loaded_key, input_to_decrypt)
    except Exception:
        # Handle exceptions and print an error message
        print(f'{Fore.RED}[+] Please make sure to specify a valid file.')
    else:
        # Print a success message if decryption is successful
        print(f'{Fore.GREEN}[+] {input_to_decrypt} Decrypted Successfully.')

# Invalid input.
else:
    print(f'{Fore.RED}[-] Invalid Input!')
    sys.exit()
