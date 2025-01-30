def encrypt(txt,n):
	encryption=""
	for i in txt:
		if i.isupper():
			encryption+=chr((ord(i)+n-65)%26+65)
		elif i.islower():
			encryption+=chr((ord(i)+n-97)%26+97)
		else:
			txt+=i
            
	return encryption

def decrypt(encrypt_txt,n):
	decryption=""
	for i in encrypt_txt:
		if i.isupper():
			decryption+=chr((ord(i)-n-65)%26+65)
		elif i.islower():
			decryption+=chr((ord(i)-n-97)%26+97)
		else:
			encrypt_txt+=i
	return decryption


txt=input("Enter any string of your choice")
key=int(input("Enter any key of your choice"))
enc_txt=encrypt(txt,key)
print("encrypted text is :"+enc_txt)
dec_txt=decrypt(enc_txt,key)
print("decrypted text is :"+dec_txt)
