# How to Use
- Install the required libraries:
```
$ pip install -r requirements.txt
```
- Available scripts:
    1. `simple_hashing.py`: Performing simple hashing algorithms using `hashlib`.
    2. `benchmark_speed.py`: Calculating the time it takes for each hashing algorithm to complete, with the help of the `timeit` module.
    3. `crack_hashes.py`: Performing brute-force on a specified hash algorithm:
        ```
        $ python crack_hashes.py 6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090 rockyou.txt --hash-type sha256
        [*] Cracking hash 6ca13d52ca70c883e0f0bb101e425a89e8624de51db2d2392593af6a84118090 using sha256 with a list of 14344394 words.
        Cracking hash:  96%|███████████████████████████████████████████████████████████████████████████████████████████▉    | 13735317/14344394 [00:20<00:00, 664400.58it/s]
        [+] Found password: abc123
        ```