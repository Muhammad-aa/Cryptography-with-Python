# Import Necessary Libraries.
import zipfile, sys
from colorama import Fore, init
from tqdm import tqdm

# Initialize Colorama.
init()

# Accept arguments from the Command line.
zip_file = zipfile.ZipFile(sys.argv[1])
wordlist = sys.argv[2]

# Calculate the number of passwords in the wordlist. (rockyou.txt)
word_list_length = len(list(open(wordlist, 'rb')))

# Open the wordlist and try each password.
with open(wordlist, 'rb') as word_list:
    print(f"{Fore.GREEN}[+] Testing all {word_list_length} Passwords... Please wait!")
    for each_word in tqdm(word_list, total=word_list_length, unit='each_word'):
        try:
            zip_file.extractall(pwd = each_word.strip())
        except:
            continue
        else:
            print(f"{Fore.GREEN}[+] Password found: {Fore.MAGENTA}{each_word.decode()}" )
            sys.exit()

print(f"{Fore.RED}[-] Password not found")