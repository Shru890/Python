gift=input()
k=int(input())
gift=list(gift)
gift=set(sorted(gift))
l=[]
for i in gift:
    if len(gift)==1:
        print(ord(i)%97)
    if len(gift)!=1:
        l.append((ord(i)%97)-1)
        l.sort(reverse=True)
if len(gift)!=1:
    if len(l)==k:
        print(l[0])
    else:
        s=sum(l[0:k])
        print(s)
