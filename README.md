# Programs Built in the [Cryptography with Python](https://thepythoncode.com/cryptography-with-python-ebook)
This repository includes the programs and scripts built in the [Cryptography with Python eBook](https://thepythoncode.com/cryptography-with-python-ebook)

More Python programs will be added to this repository as the book will be constantly improved and enriched.

Each chapter folder contain the tools discussed, containing separate `README.md` and `requirements.txt` files. It is required to install the necessary libraries for that tool before running:

```
$ pip install -r requirements.txt
```

Here's the list:

## Chapter 2: Symmetric Cryptography
- [`symmetric_cryptography.py`](Chapter-2/): A script that uses the `cryptography` library to perform asymmetric encryption (AES) on text with Python.
## Chapter 3: Asymmetric Cryptography
- [`rsa_from_scratch.py`](Chapter-3/rsa_from_scratch.py): Implements the RSA algorithm from scratch.
- [`asymmetric_cryptography.py`](Chapter-3/asymmetric_cryptography.py): Implements RSA with the `cryptography` library.
- [`elliptic_curve.py`](Chapter-3/elliptic_curve.py): Implements Elliptic Curve with the `cryptography` library.
## Chapter 4: Cryptographic Hash Functions
- [`simple_hashing.py`](Chapter-4/simple_hashing.py): Performing simple hashing algorithms using `hashlib`.
- [`benchmark_speed.py`](Chapter-4/benchmark_speed.py): Calculating the time it takes for each hashing algorithm to complete, with the help of the `timeit` module.
- [`crack_hashes.py`](Chapter-4/crack_hashes.py): Performing brute-force on a specified hash algorithm.
## Chapter 5: Message Authentication and Digital Signatures
- [`generate_and_verify_signatures.py`](Chapter-5/): Generates and verifies digital signatures with the help of the `cryptography` library.
## Chapter 6: Practical Cryptography Projects
- [`caesar_cipher.py`](Chapter-6/caesar-cipher/caesar_cipher.py): Encrypts a plaintext with the Caesar cipher.
- [`crack_caesar_cipher.py`](Chapter-6/caesar-cipher/crack_caesar_cipher.py): Cracks the Caesar cipher.
- [`affine_cipher.py`](Chapter-6/affine-cipher/affine_cipher.py): Encrypts a plaintext with the Affine cipher.
- [`affine_cipher_decrypt.py`](Chapter-6/caesar-cipher/crack_caesar_cipher.py): Cracks the Affine cipher.
- [`pdf_locker.py`](Chapter-6/pdf-locking-and-cracking/pdf_locker.py): Protects a PDF document with a password.
- [`pdf_cracker_pymupdf.py`](Chapter-6/pdf-locking-and-cracking/pdf_cracker_pymupdf.py): Performs brute-force trying to crack a password-protected PDF file.
- [`zip_file_locker.py`](Chapter-6/zipping/zip_file_locker.py): Compresses a set of files into a ZIP file with a password.
- [`adding_password_to_zip.py`](Chapter-6/zipping/adding_password_to_zip.py): Protects an already existing ZIP file with a password.
- [`zip_file_cracker.py`](Chapter-6/zipping/zip_file_cracker.py): Uses the `zipfile` standard library to perform brute-force on the ZIP file trying to crack the ZIP file password.
- [`password_manager.py`](Chapter-6/password-manager/): A CLI-based password manager that allows you to store your passwords for different websites.
- [`file_encryption_utility.py`](Chapter-6/file-encryption-and-validation/file_encryption_utility.py): Encrypting files with AES using the `cryptography` library.
- [`file_validator.py`](Chapter-6/file-encryption-and-validation/file_validator.py): Validates the checksum of a downloaded file from the Internet.
- [`ransomware.py`](Chapter-6/ransomware/): A program that encrypts entire folders with a key derived from a password.