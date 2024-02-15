# How to Use
0. Install the required libraries:
```
$ pip install -r requirements.txt
```
1. For PDF Locking:
```
$ python pdf_locker.py
Enter the path to the PDF file: Ethical-Hacking-With-Python.pdf
```
2. For cracking the `foo-protected.pdf` file using the `rockyou.txt` wordlist:
```
$ python pdf_cracker.py foo-protected.pdf rockyou.txt
Guessing password:  90%|██████████████████████ | 12844293/14344391 [14:45<01:43, 14503.59it/s]
[+] Password found: abc123
```
