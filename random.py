#to count the occurence of items in a list
li=list(map(int,input("Enter the is list values::").split(" ")))
n=len(li)
dic={x:li.count(x) for x in range(n)}
dic={x:y for x,y in dic.items() if y!=0}
print(dic)

#alphabet rangoli
import string
def print_rangoli(size):
    from string import ascii_lowercase as chars
    heap = [(('-'.join(chars[i:n])[::-1]+'-'.join(chars[i:n])[1:])).center(4*n-3, '-')   for i in range(n)]
    print(*(heap[::-1]+heap[1:]), sep="\n")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#minion game hackerrank
 vowel =['A','E','I','O','U']
    S=0
    K=0
    for i in range(len(string)):
        if string[i] in vowel:
            K+= len(string)-i
        else:
            S+=len(string)-i
    if S>K:
        print("Stuart"+" "+ "%d" % S)
    elif K>S:
        print("Kevin"+" "+'%d' % K)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)

#to perform set operations and give the sum of ramaining values in the set
n = int(input())
s = set(map(int, input().split()))
N=int(input())

for i in range(N) :
    choice=input().split()
    if choice[0]=="pop" :
        s.pop()
    elif choice[0]=="remove" :
        s.remove(int(choice[1]))
    elif choice[0]=="discard" :
        s.discard(int(choice[1]))
    else:
        print("error")
print(sum(s))

#to give all possible permutations of a word in the give set group
from itertools import permutations
l=list(map(str,input().split(" ")))
s=list(permutations(l[0],int(l[1])))
s.sort()
[print("".join(i)) for i in s]

#all possible combinations of a string
from itertools import combinations
s = input().split()
string, number = sorted(s[0]), int(s[1])
for i in range(1, number + 1):
    print(*list(map(''.join,combinations(string, i))), sep='\n')
    
#multiple of 2
n=int(input())
for i in range(n):
    if n/2==2:
        print ("True")
        break
    elif (n/2)>2:
        n=n/2
    else: 
        print("False")
        break
       #OR
    
import math
n=int(input())
a= math.log(n,2)
if 2**round(a)==n:
    print("True")
else:
    print("False")
    
#consecutive ones
def convert(n):
    b=bin(n).replace("0b","")
    b=b.split("0")
    count=len(b[0])
    for i in range(len(b)):
        if len(b[i])>count:
            count=len(b[i])
        else:
            continue
    return count

if __name__ == '__main__':
    n=int(input())
    print(convert(n))

#Count Valleys 
def countingValleys(steps, path):
    count =0
    valley = 0

    for step in path:
        if step == 'U':
            count = count + 1
        else:
            count = count - 1
        
        if step == 'U' and count == 0:
            valley += 1
    
    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

# reverse a string without inbuilt functions
a="shruti"
b=""
for i in a:
    b=i+b
print(b)

# if 153=1**3+5**3+3**3 return true
n=int(input())
n=str(n)
m=len(n)
s=0
for i in n:
    s+=int(i)**m
print('true') if s==int(n) else print("false")

#fahrenheit to celsius
def fahrenheitToCelsius(l):
    s=l[0]
    e=l[1]
    w=l[2]
    for i in range(s,e+1,w):
        celsius = int((i-32)* 5/9)
        print("{} {}".format(i,celsius))
n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split(" "))))
for i in l:    
    fahrenheitToCelsius(i)
