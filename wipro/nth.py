#for the given input number provide output as the sum of the smallest and largest number formed by rearranging the given digit.
#Input: 405
#Output: 585
n=input()
n=list(n)
n.sort()
m=n[::-1]
n="".join(n)
m="".join(m)
ans=int(n)+int(m)
print(ans)

#for the given array print an array with sum of each element.
#Input: 5
#       1 4 2 6 3
#Output: 1 5 7 13 16
n=int(input())
l=list(map(int,input().split()))
s=0
li=[]
for i in l:
  s=s+i
  li.append(s)
print("".join(map(str,li)))
