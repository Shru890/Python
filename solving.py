# find nonrepeating vowels in a string
vowels=["A","E","I","O","U","a","e","i","o","u"]
d=[]
l=list(map(str,input()))
for i in range(len(l)):
    for j in range(len(vowels)):
        if l[i]==vowels[j]:
            d.append(l[i])
u=[i for i in d if d.count(i)==1]
print(" ".join(u))

# for list commands
if __name__ == '__main__':
    N = int(input())
    L=[]
    for _ in range(N): 
        s = input().split()
        if len(s)==1: 
            cmd =s[0] 
        if len(s)==2: 
            cmd = s[0] 
            e = int(s[1]) 
        if len(s)==3: 
            cmd=s[0] 
            i = int(s[1]) 
            e = int(s[2])  

        if cmd=="insert":
            L.insert(i,e)
        elif cmd=="remove":
            L.remove(e)
        elif cmd=="append":
            L.append(e)
        elif cmd=="sort":
            L.sort()
        elif cmd=="pop":
            L.pop()
        elif cmd=="reverse":
            L.reverse()
        elif cmd=="print":
            print(L)
        else:
            print("wrong input")

# Rearrange the words according to preferences
l=list(map(str,input(" ")))
k=[i for i in l if i.isdigit()==True]
v=[i for i in l if i.isalpha()==True or i==" "]
s=("".join(v))
lv=list(s.split(" "))
dic = {k[i]: lv[i] for i in range(len(k))} 
a=sorted(list(dic.keys()))
for i in range(len(a)):
    print(dic[a[i]],end=" ")
#or
s=input().split()
d=""
for i in range(len(s)):
    for j in range(len(s)):
        if str(i) in s[j]:
            d+=s[j].replace(str(i),"")+" "
print(d)
'''
input: i1s Th0is Te2st a3
output: This is a Test
'''

# write a fuction to add element till nth term
s= input()
def add_it_up(s):
    if s.isdigit():
        s=int(s)
        sele=0
        ele=[i for i in range(s+1)]
        for i in ele:
            sele+=i
        return (sele)
    else:
        return 0

print(add_it_up(s))

#to rotate a list
n=int(input())
arr=list(map(int,input().split(" ")))
d=int(input())
def rot(arr,n,d):
    c=arr[d:]+arr[0:d]
    for i in range(n):
        arr[i]=c[i]
rot(arr,n,d)
print(arr)

#get the max numbers
li=sorted(map(int,input().split(" ")))
n=int(input())
li=li[-n:]
li.reverse()
print(li)

#itertools-groupby
from itertools import groupby
s= input()
for k, g in groupby(s):
    l= list(g)
    print("({}, {})".format(len(l), k), end=" ")
    
# to check anagram
a,b=input().split(',')
a=sorted(list(a))
b=sorted(list(b))
if len(a)==len(b):
    for i in range(len(a)):
        if a[i]==b[i]:
            c=1
        else:
            c=0
    if c==1:
        print("True")
    else:
        print("False")
else:
    print("Unequal input lengths")
    
#Sub list of sum equals to zero
li=[]
l=list(map(int, input().split(" ")))
for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k]==0:
                dum=[l[i],l[j],l[k]]
                li.append(dum)
            else:
                continue
print(li)

#min-max sum
def miniMaxSum(arr):
    arr=sorted(arr)
    n=len(arr)
    print(sum(arr[:n-1]),sum(arr[1:]))
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
    
#Birthday cake candles
def birthdayCakeCandles(candles):
    candles=sorted(candles)
    count=0
    tallcandle=max(candles)
    for i in candles:
        if i==tallcandle:
            count+=1
    return count

#print all strings of n bits
n=int(input())
l=[]
for i in range(2**n):
    l.append(bin(i).replace("0b",""))
    if len(l[i])<n:
        l[i]="0"*(n-len(l[i]))+l[i]
print("\n".join(l))
