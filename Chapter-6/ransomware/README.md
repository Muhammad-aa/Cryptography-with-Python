# How to Use
0. Install `cryptography` library via pip:
```bash
$ pip install -r requirements.txt
```
1. Given a folder named `test-folder`, you can encrypt it via the following command:
```
$ python ransomware.py -e test-folder -s 32
Enter the password for encryption: 
```
You'll be prompted for the password to encrypt, input one and you'll see output like this:
```
[*] Encrypting test-folder\Documents\free-Chapter 1_ Introduction-to-PDF-Processing-in-Python.pdf
[*] Encrypting test-folder\Documents\free-Chapter_2_Building_Malware.pdf
[*] Encrypting test-folder\Files\Archive\my-archive.zip
[*] Encrypting test-folder\Files\Programs\7z2107-x64.exe
[*] Encrypting test-folder\Pictures\cat face flat.jpg
[*] Encrypting test-folder\Pictures\cute_dog_flat_light.png
[*] Encrypting test-folder\test.txt
[*] Encrypting test-folder\test2.txt
[*] Encrypting test-folder\test3.txt
```
2. To decrypt the folder, put the same password used for encryption:
```
$ python ransomware.py test-folder -d
Enter the password you used for encryption: 
```
The password won't be shown, as it's using the `getpass` module. Here's a similar output if you get the password wrong:
```
[*] Decrypting test-folder\Documents\free-Chapter 1_ Introduction-to-PDF-Processing-in-Python.pdf
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\Documents\free-Chapter_2_Building_Malware.pdf
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\Files\Archive\my-archive.zip
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\Files\Programs\7z2107-x64.exe
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\Pictures\cat face flat.jpg
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\Pictures\cute_dog_flat_light.png
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\test.txt
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\test2.txt
[!] Invalid token, most likely the password is incorrect
[*] Decrypting test-folder\test3.txt
[!] Invalid token, most likely the password is incorrect
```
And this if you get it right:
```
[*] Decrypting test-folder\Documents\free-Chapter 1_ Introduction-to-PDF-Processing-in-Python.pdf
[*] Decrypting test-folder\Documents\free-Chapter_2_Building_Malware.pdf
[*] Decrypting test-folder\Files\Archive\my-archive.zip
[*] Decrypting test-folder\Files\Programs\7z2107-x64.exe
[*] Decrypting test-folder\Pictures\cat face flat.jpg
[*] Decrypting test-folder\Pictures\cute_dog_flat_light.png
[*] Decrypting test-folder\test.txt
[*] Decrypting test-folder\test2.txt
[*] Decrypting test-folder\test3.txt
```