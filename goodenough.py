'''
Only x hours are left for the March Long Challenge and Chef is only left with the last problem unsolved. However, he is sure that he cannot solve the problem in the remaining time.
From experience, he figures out that he needs exactly H hours to solve the problem.
Now Chef finally decides to use his special power which he has gained through years of intense yoga.
He can travel back in time when he concentrates.
Specifically, his power allows him to travel to N different time zones, which are T1,T2,…,TN hours respectively behind his current time.

Input
The first line of the input contains three space-separated integers N, H and x.
The second line contains N space-separated integers T1,T2,…,TN.

Output
Print a single line containing the string "YES" if Chef can solve the problem on time or "NO" if he cannot.
You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

'''
ans=[]
n,h,x=map(int,input().split(" "))
l = list(map(int,input().split(" ")))[:n] 
for i in range(len(l)):
    if(x+l[i]==h):
        ans.append(1)
    else:
        ans.append(0)
if any(ans)==True:
    print("yes")
else:
    print("no")
