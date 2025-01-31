keys={'a':'z','b':'y','c':'x','d':'w','e':'v','f':'u','g':'t','h':'s','i':'r','j':'q','k':'p','l':'o','m':'n','n':'m','o':'l','p':'k','q':'j','r':'i','s':'h','t':'g','u':'f','v':'e','w':'d','x':'c','y':'b','z':'a'}
reverse_keys={}
for key,value in keys.items():
    reverse_keys[value]=key
    #the commented code can be used when user requires to give his own key
    # alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    # map={}
    # print("enter the mapping ")
    # for i in range(26):
        # keys=input("encryption Value: ")
        # map[alpha[i]]=keys
def encrypt(text):
    text=str(text)
    encrypting=[]
    for l in text:
        encrypting.append(keys.get(l,l))
    return ''.join(encrypting)
    
def decipher(text):
    text=str(text)
    decrypted=[]
    for l in text:
        decrypted.append(reverse_keys.get(l,l))
    return ''.join(decrypted)
    
x=input("enter the plain text ")
print("encrypted: ",encrypt(x))
print("decrypted: ",decipher(encrypt(x)))