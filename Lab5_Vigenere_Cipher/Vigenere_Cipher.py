
def vigenere_cipher(plain,key):
    plain=plain.lower().replace(" ","")
    m=len(key)
    cipherText=""
    for i in range(len(plain)):
        letter=plain[i]
        k=key[i%m]
        cipherText+=chr((ord(letter)+k-97)%26+97)
    return cipherText
plain=input("Enter the plain text ")
key_text=input("enter the key text ")  
key=[ord(i)-ord('a') for i in key_text]
cipher=vigenere_cipher(plain,key)
print("CIPHER TEXT: ",cipher)
rev_key=[-1*k for k in key]
print("Deciphered plain text: ",vigenere_cipher(cipher,rev_key))

