import json, hashlib, getpass, os, pyperclip
from cryptography.fernet import Fernet


# Function for Hashing the Master Password.
def hash_password(password):
    sha256 = hashlib.sha256()
    sha256.update(password.encode())
    return sha256.hexdigest()


# Generate a secret key. This should be done only once as you'll see.
def generate_key():
    return Fernet.generate_key()


# Initialize Fernet cipher with the provided key.
def initialize_cipher(key):
    return Fernet(key)


# Function to encrypt a  password.
def encrypt_password(cipher, password):
    return cipher.encrypt(password.encode()).decode()


# Function to decrypt a  password.
def decrypt_password(cipher, encrypted_password):
    return cipher.decrypt(encrypted_password.encode()).decode()

# Function to register a user.
def register(username, master_password, key):
    # Hash the master password before storing it
    hashed_master_password = hash_password(master_password)
    user_data = {'username': username, 'master_password': hashed_master_password}
    with open('user_data.json', 'w') as file:
        json.dump(user_data, file)


# Function to log you in.
def login(username, entered_password):
    with open('user_data.json', 'r') as file:
        user_data = json.load(file)

    stored_password_hash = user_data.get('master_password')
    entered_password_hash = hash_password(entered_password)

    if entered_password_hash == stored_password_hash and username == user_data.get('username'):
        return True
    else:
        return False


# Function to view saved websites.
def view_websites():
    with open('passwords.json', 'r') as data:
        view = json.load(data)
        print("Websites you saved...\n")
        for x in view:
            print(x['website'])
        print('\n')


# Load or generate the encryption key
key_filename = 'encryption_key.key'
if os.path.exists(key_filename):
    with open(key_filename, 'rb') as key_file:
        key = key_file.read()
else:
    key = generate_key()
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)

cipher = initialize_cipher(key)


def add_password(website, password):
    # Check if passwords.json exists
    if not os.path.exists('passwords.json'):
        # If passwords.json doesn't exist, initialize it with an empty list
        data = []
    else:
        # Load existing data from passwords.json
        try:
            with open('passwords.json', 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            # Handle the case where passwords.json is empty or invalid JSON.
            data = []

    # Encrypt the password
    encrypted_password = encrypt_password(cipher, password)

    # Create a dictionary to store the website and password
    password_entry = {'website': website, 'password': encrypted_password}
    data.append(password_entry)

    # Save the updated list back to passwords.json
    with open('passwords.json', 'w') as file:
        json.dump(data, file, indent=4)


def get_password(website):
    # Check if 'passwords.json' exists
    if not os.path.exists('passwords.json'):
        return None

    # Load existing data from 'passwords.json'
    try:
        with open('passwords.json', 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        data = []

    for entry in data:
        if entry['website'] == website:
            # Decrypt and return the password
            decrypted_password = decrypt_password(cipher, entry['password'])
            return decrypted_password

    return None

# Infinite loop to keep the program running until the user chooses to quit.
while True:
    print("1. Register")
    print("2. Login")
    print("3. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':  # If a user wants to register
        file = 'user_data.json'
        # Check if user_data.json exists and is empty
        if os.path.exists(file) and os.path.getsize(file) == 0:
            username = input("Enter your username: ")
            master_password = getpass.getpass("Enter your master password: ")

            # Call the register function to store user data securely
            register(username, master_password, key)
            print("[+] Registration successful!")
        else:
            print("[-] Master user already exists.")

    elif choice == '2':  # If a User wants to log in
        username = input("Enter your username: ")
        master_password = getpass.getpass("Enter your master password: ")
        user_data = login(username, master_password)

        if user_data:  # Successful login
            print("[+] Login successful!")

            while True:
                print("1. Add Password")
                print("2. Get Password")
                print("3. View Saved websites")
                print("4. Quit")
                password_choice = input("Enter your choice: ")

                if password_choice == '1':  # If a user wants to add a password
                    website = input("Enter website: ")
                    password = getpass.getpass("Enter password: ")

                    # Encrypt and add the password
                    add_password(website, password)
                    print("[+] Password added!")

                elif password_choice == '2':  # If a User wants to retrieve a password
                    website = input("Enter website: ")
                    decrypted_password = get_password(website)
                    if website and decrypted_password:
                        # Copy password to clipboard for convenience
                        pyperclip.copy(decrypted_password)
                        print(f"[+] Password for {website}: {decrypted_password}\n[+] Password copied to clipboard.")
                    else:
                        print("[-] Password not found! Did you save the password?")

                elif password_choice == '3':  # If a user wants to view saved websites
                    view_websites()

                elif password_choice == '4':  # If a user wants to quit the password manager
                    break

        else:  # Login failed
            print("[-] Login failed. Incorrect master password!")

    elif choice == '3':  # If a user wants to quit the program
        break
