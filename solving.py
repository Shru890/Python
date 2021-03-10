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
