def encrypt(txt,n):
	encryption=""
	for i in txt:
		if i.isalpha():
			encryption+=chr(ord(i)+n)
		else:
			txt+=i
            
	return encryption

def decrypt(encrypt_txt,n):
	decryption=""
	for i in encrypt_txt:
		if i.isalpha():
			decryption+=chr(ord(i)-n)
		else:
			encrypt_txt+=i
	return decryption


txt=input("Enter any string of your choice")
key=3
enc_txt=encrypt(txt,key)
print("encrypted text is :"+enc_txt)
dec_txt=decrypt(enc_txt,key)
print("decrypted text is :"+dec_txt)
