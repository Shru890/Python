import random
import math
pt=input("Enter text or number to be encrypted:")
if pt.isalpha():
    pta=pt.lower()
    ptn=[ord(i)%97 for i in pta]
elif pt.isdigit():
    ptn=int(pt)

n=int(input("Enter a composite prime number:"))
prime=[2,3,5,7,11,13,17,19,23,29,31,33,37,41,43,47,53,57,61,67,69,71,73,77,81,83,87,91,97]
for i in prime:
    if n%i == 0:
        p=i
        q=n//i
        break
phi=(p-1)*(q-1)
e= 0
for i in range(2,26):
    if math.gcd(i,phi)==1:
        e=i
        break
def modInverse(a,m):
    for x in range(1, m):
        if (((a%m) * (x%m)) % m == 1):
            return x
    return -1

d = modInverse(e,phi)
if d!= -1:
    if pt.isalpha():
        ct= [(i**e)%n for i in ptn]
        print("Encrypted value::",*ct)
        dt= [(i**d)%n for i in ct]
    else:
        ct = (ptn**e) % n 
        dt = (ct**d) % n
else:
    print("Invalid Key Encryption is not Possible!!!!!!!!")
    
if pt.isalpha() and pt.islower():
    dt = "".join([chr(97+int(i)) for i in dt])
elif pt.isalpha and pt.isupper():
    dt = "".join([chr(65+int(i)) for i in dt])
else:
    dt= dt
print("Decrypted value::",dt)
