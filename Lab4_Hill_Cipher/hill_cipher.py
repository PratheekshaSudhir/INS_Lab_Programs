import numpy as np

def text_to_numbers(text):
    return [ord(char)-ord('A') for char in text]

def numbers_to_text(numbers):
    return ''.join(chr(num+ord('A')) for num in numbers )

def encrypt_hill(plain,key_mat):
    cipher_num=[]
    n=len(key_mat)
    print(n)
    plain=plain.upper().replace(" ","")
    while (len(plain)%n !=0):
        plain=plain+"X"
    
    plain_num=text_to_numbers(plain)
    for i in range(0,len(plain_num),n):
        vector=np.array(plain_num[i:i+n])
        cipher_inter=np.dot(key_mat,vector)%26
        cipher_num.extend(cipher_inter)
        
    return numbers_to_text(cipher_num)

plain=input("enter the plain text to encrypt ")
#key_text=input("enter the key")
#m=int(input("Enter the dimension of the key"))
#while(len(key_text)% (m*m)  !=0):
#    key_text+="X"
#key1=text_to_numbers(key_text)
#key_mat=np.array(key1).reshape(m, m)
#print(key_mat)
# for i in range(0,len(key_text),m):
#     key_vector=np.array(key_text[i:i+m])
#     key_mat.extend(key_vector)
key=[[7,8],[11,11]]
print("Cipher Text: ",encrypt_hill(plain,key))
