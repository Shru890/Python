def is_armstrong_number(number):
    number=str(number)
    n=len(number)
    s=0
    r=[int(x)**n for x in number]
    for i in r:
        s+=i
    s=str(s)
    if number==s:
        return (True)
    else:
        return (False)
number=int(input())
ans=is_armstrong_number(number)
print(ans)
