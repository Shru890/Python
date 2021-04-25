def convert(number): 
    ans = "" 
    if number % 3 == 0: ans += 'Pling' 
    if number % 5 == 0: ans += 'Plang' 
    if number % 7 == 0: ans += 'Plong'
    if number % 3 !=0 and number % 5 !=0 and number % 7 !=0: ans=str(number)
    return ans
number=int(input())
ans=convert(number)
print(ans)
