# Import the necessary modules for cryptography.
from cryptography.hazmat.primitives import hashes  # Import the hash function.
from cryptography.hazmat.primitives.asymmetric import padding  # Import the padding function.
from cryptography.hazmat.primitives.asymmetric import rsa  # Importing RSA cryptographic functions.
from colorama import init, Fore  # Import colorama for colored output.

init()  # Initialize colorama for terminal color formatting.

# Generate private and public keys using the RSA algorithm.
private_key = rsa.generate_private_key(  # Generate an RSA private key.
    public_exponent=65537,  # Set the public exponent for the key.
    key_size=2048  # Define the key size as 2048 bits.
)
public_key = private_key.public_key()  # Obtain the public key from the private key.

# Define the messages to be signed and used for verification.
message = b"Secret message to be signed"  # The first message to be signed.
message2 = b"Second Message that is not signed"  # A different, unsigned message for verification.

# Sign the message using the private key.
signature = private_key.sign(
    message,  # Message to be signed.
    padding.PSS(  # Use PSS padding scheme with SHA-256 hashing.
        mgf=padding.MGF1(hashes.SHA256()),  # Specify the Mask Generation Function.
        salt_length=padding.PSS.MAX_LENGTH  # Define salt length for padding.
    ),
    hashes.SHA256()  # Specify the hash algorithm as SHA-256.
)

# Verify the signature using the public key.
try:
    public_key.verify(
        signature,  # The signature to be verified.
        message,  # A different, unsigned message for verification.
        padding.PSS(  # Use the same padding and hashing algorithm.
            mgf=padding.MGF1(hashes.SHA256()),  # Specify the Mask Generation Function.
            salt_length=padding.PSS.MAX_LENGTH  # Define salt length for padding.
        ),
        hashes.SHA256()  # Specify the hash algorithm as SHA-256.
    )
    print(f"{Fore.GREEN}Signature verified: The message is authentic.")  # Print verification success in green.

except Exception:
    print(f"{Fore.RED}Signature verification failed: The message may have been tampered with.")  # Print verification failure in red.
