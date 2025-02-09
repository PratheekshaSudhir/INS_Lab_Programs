# Vigenère Cipher Encryption and Decryption
## Overview
This is a Python implementation of the Vigenère Cipher, a classical encryption technique that uses a repeating keyword to shift letters in the plaintext. This script allows users to encrypt and decrypt messages using a given key.

## Features
- Encrypts plaintext using a repeating keyword.
- Decrypts ciphertext back to its original plaintext.
- Ignores non-alphabetical characters, preserving them in the output.

## How It Works
### Encryption
- Convert plaintext and key to uppercase.
- Repeat the key to match the length of the plaintext.
- Shift each letter of the plaintext forward based on the corresponding key letter.
### Decryption
- Convert ciphertext and key to uppercase.
- Use the key to shift letters in the ciphertext backward to retrieve the original plaintext.

## Running the Code
1) Clone the repository:
```ssh
git clone https://github.com/yourusername/vigenere-cipher.git
cd vigenere-cipher
```
2) Run the script:
```ssh
python vigenere_cipher.py
```
## Link to Codespaces
https://animated-happiness-5ggxg95pw6gpf4vrx.github.dev/
