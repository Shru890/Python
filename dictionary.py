#to count the occurence of items in a list
li=list(map(int,input("Enter the is list values::").split(" ")))
n=len(li)
dic={x:li.count(x) for x in range(n)}
dic={x:y for x,y in dic.items() if y!=0}
print(dic)

