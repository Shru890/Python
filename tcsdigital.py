#Remove the self repeating digit numbers (ex. 11, 22,...., 111, 222,...)
'''
Input:
11
15
Output:
4
'''
n1=int(input())
n2=int(input())
l2=[i for i in range(11,(11*10)+1,11)]
l3=[i for i in range(111,(111*10)+1,111)]
l4=[i for i in range(1111,(1111*10)+1,1111)]
l=[i for i in range(n1,n2+1)]
nf=len(str(n1))
ns=len(str(n2))
if nf==ns==2:
    for element in l2:
        if element in l:
            l.remove(element)
elif nf==ns==3:
    for element in l3:
        if element in l:
            l.remove(element)
elif nf==ns==4:
    for element in l4:
        if element in l:
            l.remove(element)
elif nf==2 and ns==3:
    l5=l2+l3
    for element in l5:
        if element in l:
            l.remove(element)
elif nf==3 and ns==4:
    l6=l3+l4
    for element in l6:
        if element in l:
            l.remove(element)
else:
    for element in l2:
        if element in l:
            l.remove(element)
print(len(l))

# Rotate the array by the given number excluding the first element
'''
Input:
5
10, 20, 30, 40, 50
2
Output:
10, 40, 50, 20, 30
'''
n=int(input())
l=[int(input()) for i in range(n)]
k=int(input())
for i in range(k):
    l.insert(1,l[-1])
    l.pop()
s=""
for i in l:
    s=s+" "+str(i)
s=s.lstrip()
print("".join(s))
