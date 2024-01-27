import hashlib # Import the hashlib lab for hashing.
from colorama import init, Fore # Import colorama for colored output.

# Initialize colorama.
init()

# Creating a SHA-256 hash object.
hash_object = hashlib.new('sha256')

# Data to be hashed.
data_to_hash = b'thepythoncode.com'

# Updating the hash object with the data.
hash_object.update(data_to_hash)

# Retrieving the hash value in hexadecimal format.
hash_result = hash_object.hexdigest()

# Print out the hashed value.
print(f"{Fore.GREEN}Hash Result: {hash_result}")
