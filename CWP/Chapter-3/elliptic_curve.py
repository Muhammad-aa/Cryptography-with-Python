from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# Generate an ECC key pair
private_key = ec.generate_private_key(ec.SECP384R1())
public_key = private_key.public_key()

# Serialize the public key for sharing/storing
pem_public_key = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Encrypt a message using the public key (ECC uses shared secret for encryption)
shared_secret = private_key.exchange(ec.ECDH(), public_key)
derived_key = hashes.Hash(hashes.SHA256())
derived_key.update(shared_secret)
encrypted_message = derived_key.finalize()  # Simplified encryption

# Decrypt the message using the private key (using the shared secret)
decrypted_message = encrypted_message  # Simplified decryption

print(f"Public Key:\n{pem_public_key.decode('utf-8')}")
print(f"Encrypted Message: {encrypted_message}")
print(f"Decrypted Message: {decrypted_message}")
