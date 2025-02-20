# Feistel Cipher 

## Overview
This repository contains a simple implementation of the Feistel Cipher, a symmetric encryption technique based on multiple rounds of substitution and permutation. This implementation uses a basic round function that sums the ASCII values of the right half of the text and a key, then performs an XOR operation for encryption and decryption.

## Features
✅ Encryption: Encrypts plaintext using a Feistel network with multiple rounds.
✅ Decryption: Reverses encryption using the same round keys in reverse order.
✅ Padding Handling: Ensures even-length plaintext by appending "X" if necessary.
✅ Simple Round Function: Uses a sum-based function for educational purposes.

## How the Round Function Works
Each round in the Feistel cipher applies a transformation to the text. The round function used in this implementation is:
```ssh
round_function = (sum(ord(c) for c in R) + K) % 256
```
### Steps:
1) Sum ASCII Values: The function calculates the sum of ASCII values of characters in the right half (R).
2) Add the Round Key (K): The key for the current round is added.
3) Modulo 256: The sum is taken modulo 256 to keep values within a valid range.
4) XOR Operation: The left half (L) is XORed with the result of the round function to generate a new right half.

### Encryption Process
- Ensure Even Length: If the plaintext length is odd, append "X".
- Split into Two Halves: Divide plaintext into L (left) and R (right).
- Apply Feistel Rounds: Use the round function iteratively with the given keys.
- Concatenate Final Halves: The output of the last round forms the ciphertext.
### Decryption Process
- Split Ciphertext into Halves (L and R).
- Apply Feistel Rounds in Reverse Order: Using the round keys in reverse.
- Swap Back Each Round: Restore original halves step by step.
- Remove Padding (X): Retrieve the original plaintext.

## How to Use this Code
1. Clone the Repository:
```ssh
git clone https://github.com/yourusername/feistel-cipher.git
cd feistel-cipher
```
2. Run the Script:
```ssh
python feistel_cipher.py
```
3. Enter Input:
```ssh
enter the plain text: HELLO
```

## Output Example:
```ssh
Plaintext:  HELLO
Ciphertext:  ÙÔÝñòå
Decrypted:  HELLO
```

## Link to Codespaces
You can also run this in GitHub Codespaces:
https://animated-happiness-5ggxg95pw6gpf4vrx.github.dev/