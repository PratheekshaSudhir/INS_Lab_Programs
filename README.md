# Caesar Cipher Encryption and Decryption

## Overview
This is a simple implementation of the Caesar Cipher, a basic encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet. This script provides functions to both encrypt and decrypt a given text using a specified shift value.

## Features

1) Encrypts a given text using a Caesar cipher.

2) Decrypts the encrypted text back to its original form.

3) Handles both uppercase and lowercase letters correctly.

4) Ignores non-alphabetic characters in the shift process.

## How It Works
The encrypt() function takes a text string and a shift value (n) and shifts each letter forward by n positions within the alphabet.
The decrypt() function reverses the process by shifting the letters back by n positions.

## Usage
- Encryption

  1) Enter a string when prompted.

  2) Enter a numeric key value for the shift.

  3) The function shifts each character by the defined key.

  4) The encrypted text is displayed.

- Decryption

  1) The encrypted text is passed to the decrypt() function.

  2) The function shifts each character back to its original position.

  3) The decrypted text is displayed.
 
## Code Inference
Enter the text: pizza

enter the key: 1

encrypted text: qjaab

decrypted text: pizza

## Output image

![image](https://github.com/user-attachments/assets/89c31c9b-7673-4bde-8885-5fd6b15e6bb1)






