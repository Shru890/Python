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
