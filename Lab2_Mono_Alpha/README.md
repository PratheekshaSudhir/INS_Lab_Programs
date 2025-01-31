# Monoalphabetic Cipher Encryption and Decryption

## Overview
This script implements a Monoalphabetic Cipher, where each letter in the plaintext is replaced with a corresponding letter from a predefined key mapping. This method ensures that the encryption remains consistent, making it a simple but effective way to obscure messages.

## Features
- Encrypts a given text using a fixed substitution cipher.
- Decrypts the encrypted text back to its original form.
- Ignores non-alphabetic characters in the substitution process.

## How It Works
The encrypt() function takes a text string and replaces each letter with its corresponding mapped letter.
The decipher() function reverses the encryption process using a reverse mapping.

## Usage

1) Encryption
- Enter a string when prompted.
- The function replaces each character according to the predefined mapping.
- The encrypted text is displayed.

2) Decryption
- The encrypted text is passed to the decipher() function.
- The function replaces each character with its original mapped letter.
- The decrypted text is displayed.

## Output image

![image](https://github.com/user-attachments/assets/8b4e94f1-1eb1-4f94-963b-9006fff627bd)


## How to Use the Code from GitHub
1) Clone the repository using:
```ssh
git clone https://github.com/yourusername/monoalphabetic-cipher.git
```
2) Navigate to the project directory:
```ssh
cd monoalphabetic-cipher
```
3) Run the script using Python:
```ssh
python monoalphabetic_cipher.py
```
4) Follow the prompts to enter text for encryption and decryption

## Codespaces link
You may use the following link to run this code in Codespaces 

https://cautious-space-memory-q77p7x6gwr4qf664p.github.dev/
