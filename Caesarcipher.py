# Python code for Caesar Cipher
string = input("Enter String:")
key = int(input("Enter key value:"))
li=[]
li2=[]
c=65
d=97
for i in range(0,26):
    li.append(chr(c))
    c=c+1 

for i in range(0,26):
    li2.append(chr(d))
    d=d+1
    
for j in string:
    if j in li:
        a = (li.index(j)+key)%26
        print(li[a].upper(),end="")
    elif j in li2:
        b = (li2.index(j)+key)%26
        print(li[b].lower(),end="")
    elif j == " ":
        print(j,end="")
