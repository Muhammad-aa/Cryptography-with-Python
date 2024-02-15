# How to Use
0. Install the required libraries for these tools:
```bash
$ pip install -r requirements.txt
```
1. For the ZIP Locker, you want to create a ZIP file named `test.zip` that contain `random-image.png` and `random-text.txt`:
```bash
$ python zip_file_locker.py --zipfile test.zip --addfile random-image.png random-text.txt
[?] Enter your password > 
[+] ZIP file is locked with a strong password.
```
2. For adding password to an existing ZIP file:
```bash
$ python adding_password_to_zip.py my-archive.zip
Enter the password for the new ZIP file: 
Password-protected ZIP file created at my-archive-protected.zip
```
3. For performing brute-force on a ZIP file named `secret.zip` using the `rockyou.txt` wordlist:
```
$ python zip_cracker.py secret.zip rockyou.txt
Total passwords to test: 14344395
  3%|▉                            | 435977/14344395 [01:15<40:55, 5665.23word/s]
[+] Password found: abcdef12345
```