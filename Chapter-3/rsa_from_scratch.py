import random
from sympy import isprime, mod_inverse


def generate_prime_candidate(length):
    """Generate a random odd integer of a specified bit length.
    
    Args:
    length: The bit length of the prime candidate.
    
    Returns:
    A random odd integer with the specified bit length."""
    # Generate a random number of the specified length
    p = random.getrandbits(length)
    # Ensure the number is odd and has the highest bit set (to maintain length)
    p |= (1 << length - 1) | 1
    return p


def generate_large_prime(length):
    """Generate a large prime number of a specified bit length.
    
    Args:
    length: The bit length of the prime number to generate.
    
    Returns:
    A prime number with the specified bit length."""
    p = 4
    # Keep generating prime candidates until a prime number is found
    while not isprime(p):
        p = generate_prime_candidate(length)
    return p


def generate_keypair(keysize):
    """Generate a public and private key pair for RSA encryption.

    Args:
    keysize: The bit length of the keys to generate.
    
    Returns:
    A tuple containing the public key and private key pairs."""
    # Generate two large prime numbers
    p = generate_large_prime(keysize)
    q = generate_large_prime(keysize)
    # Calculate the modulus for the public and private keys
    n = p * q
    # Calculate Euler's totient function (phi)
    phi = (p-1) * (q-1)
    # Choose a public exponent
    e = 65537
    # Calculate the private exponent
    d = mod_inverse(e, phi)
    # Return the public and private key pairs
    return ((e, n), (d, n))


def encrypt(pk, plaintext):
    """Encrypts a string (plaintext) using the public key (pk).
    
    Args:
    pk: A tuple containing the public key and modulus (e, n).
    plaintext: A string representing the message to be encrypted.
    
    Returns:
    A list of integers representing the encrypted message."""
    key, n = pk
    # Convert each letter in the plaintext to numbers based on the character using more efficient modular exponentiation
    cipher = [pow(ord(char), key, n) for char in plaintext]
    return cipher


def decrypt(pk, ciphertext):
    """Decrypts a list of integers (ciphertext) using the private key (pk).
    
    Args:
    pk: A tuple containing the private key and modulus (d, n).
    ciphertext: A list of integers representing the encrypted message.
    
    Returns:
    A string representing the decrypted message."""
    key, n = pk
    # Decrypt each number in the ciphertext and convert back to characters
    plain = [chr(pow(char, key, n)) for char in ciphertext]
    return ''.join(plain)


if __name__ == '__main__':
    # Key size should be large (e.g., 2048 bits) for real applications
    keysize = 64  # Smaller size used here for simplicity
    print("Generating key pair...")
    public, private = generate_keypair(keysize)
    print("Public key:", public)
    print("Private key:", private)

    message = "Hello, RSA!"
    print("Original message:", message)
    encrypted_msg = encrypt(public, message)
    print("Encrypted message:", ''.join(map(lambda x: str(x), encrypted_msg)))
    decrypted_msg = decrypt(private, encrypted_msg)
    print("Decrypted message:", decrypted_msg)
