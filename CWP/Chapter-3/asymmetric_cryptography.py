from cryptography.hazmat.primitives.asymmetric import rsa  # Importing RSA key generation functionality.
from cryptography.hazmat.primitives.asymmetric import padding  # Importing padding for encryption and decryption.
from cryptography.hazmat.primitives import hashes  # Importing hashing algorithms for encryption.
from colorama import init, Fore  # Importing color formatting for terminal output.

init()  # Initialize colorama for colored terminal output.

# Generate Key Pair.
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Commonly used public exponent
    key_size=2048  # Size of the key in bits
)

public_key = private_key.public_key()  # Obtaining the corresponding public key.

# Message to be Encrypted.
text_to_encrypt = b"Cryptography with Python"  # Original message to be encrypted.

# Encrypting the Message.
cipher_text = public_key.encrypt(
    text_to_encrypt,  # Message to be encrypted.
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function with SHA256 hash algorithm.
        algorithm=hashes.SHA256(),  # Hash algorithm for encryption.
        label=None  # Optional label for customization (set to None).
    )
)

# Decrypting the Message.
decrypted_message = private_key.decrypt(
    cipher_text,  # Encrypted message.
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),  # Mask generation function used during encryption.
        algorithm=hashes.SHA256(),  # Hash algorithm used during encryption.
        label=None  # Optional label (set to None, similar to encryption).
    )
)

# Display Information with Color.
print(f"{Fore.MAGENTA}Original Message: {text_to_encrypt}")  # Print the original message in magenta color.
print(f"{Fore.RED}Encrypted Message: {cipher_text} ", cipher_text)  # Display the encrypted message in red color.
print(f"{Fore.GREEN}Decrypted Message: {decrypted_message.decode()}")  # Display the decrypted message in green color
