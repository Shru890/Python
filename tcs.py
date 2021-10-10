# Racer Hault Code
n=int(input())
y=int(input())
li=[]
s=0
for i in range(n):
    li.append(int(input()))
for i in range(n):
    if li[i]<y:
        s = s+li[i]
    else:
        s= s+y
print(s)

#Greyhound Player Code
x=int(input())
y=int(input())
m=x+y
if m%3==0:
  print(m//3)
else:
  for i in range(m+1):
    if m%3!=0:
      m=m-1
  print(m//3)
