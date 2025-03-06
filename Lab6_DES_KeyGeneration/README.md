# DES Key Generation in Python

## Overview
This repository contains an implementation of Data Encryption Standard (DES) key generation in Python. The script takes a user-input string, converts it into a binary representation, performs bit manipulations, and generates 8 subkeys using a shift box and a randomized selection process.

## Features
✅ Binary Conversion: Converts input text into an 8-bit binary format.
✅ Bit Manipulation: Removes the first bit of every byte (sign bit) for further processing.
✅ Left-Right Splitting: Divides the processed binary into two equal halves.
✅ Bit Shifting: Uses a predefined shift box for controlled shifting.
✅ Randomized Key Selection: Generates 8 unique keys using random bit selection.

## How the Key Generation Works
### Convert Input to Binary:

1) Each character in the string is converted into an 8-bit binary representation.
Example:
```ssh
"A" → 01000001  
"B" → 01000010
```  
2) Remove the First Bit of Every Byte:Since the first bit represents the sign in ASCII, it is ignored.
Example:
```ssh
"A" (01000001) → 1000001  
"B" (01000010) → 1000010  
```
3) Split the Binary Data into Two Halves:
The remaining bits are divided into left and right parts.

4) Bit Shifting with Shift Box:
A predefined shift box (lt = [2,3,6,7,1,6,5,9]) determines how many bits are shifted.

5)Generate New Keys:
- Left and Right halves are shifted based on the shift box values.
- Randomized selection ensures uniqueness in generated keys.
- 8 unique keys are extracted for use in DES encryption.

## Example Run
🔹 Input:
```ssh
Enter a string: Hello
```
🔹 Output:
```ssh
Key 1  =  110010101...
Key 2  =  100111001...
Key 3  =  011101100...
Key 4  =  111001010...
Key 5  =  100110101...
Key 6  =  110011000...
Key 7  =  101011101...
Key 8  =  011110010...
```

## Running the Code
1️⃣ Clone the Repository
```ssh
git clone https://github.com/yourusername/des-key-generation.git
cd des-key-generation
```
2️⃣ Run the Script
```ssh
python des_key_generator.py
```
3️⃣ Enter Input
```ssh
Enter a string: Secure
```
4️⃣ View Generated DES Keys
```ssh
Key 1 = 10100110...
Key 2 = 11001001...
...
```
## Link to Codespaces
https://animated-happiness-5ggxg95pw6gpf4vrx.github.dev/