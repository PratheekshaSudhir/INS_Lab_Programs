
def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    encrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')  
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  
    return encrypted_text
def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    decrypted_text = ""
    key_length = len(key)
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  
    return decrypted_text

plaintext= input("enter the plaintext: ")
key = input("enter the key text: ")
encrypted = vigenere_encrypt(plaintext, key)
decrypted = vigenere_decrypt(encrypted, key)
print(f"Plaintext: ",plaintext)
print(f"Encrypted: ",encrypted)
print(f"Decrypted: ",decrypted)
