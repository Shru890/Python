#1.to accept a tuple from user
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s)
a=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
print(a)

#2.to make a tuple according to user specified data type
ty=input("Enter the type of tuple Ex. numeric or aplhabetic::")
if ty=="numeric":
    s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
    print(s)
else:
    a=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
    print(a)

#3.to accept a numeric tuple and print any element
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s[0])

#4.to convert tuple to string
s=tuple(map(str,input("Enter the values for alphabetic tuple::").split(" ")))
print(s)
print(" ".join(s))

#5.to accept a tuple and display it's fourth and fourth last element
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print(s[3])
print(s[-4:-3])

#6.to check element in a tuple
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
k=int(input("Enter the element::"))
print(k in s)

#7.to remove an element for a tuple
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
i=int(input("index of the element to be removed::"))
print(s)
p=list(s)
p.remove(i)
print(tuple(p))

#8.to give the length of a tuple
s=tuple(map(str,input("Enter the values for tuple::").split(" ")))
print(len(s))

#9.to convert from tuple to dictionary
li=[]
n=int(input("Enter the number of subtuple::"))
for i in range(n):
    s=map(int,input("Enter 2 tuple values::").split(" "))
    s=tuple(s)
    li.append(s)
li=dict(li)
print(li)

#10.to change the subtuple (22,3) to (222,3)
tup=(1,(22,3),4,5,6)
tup2=list(tup)
tup2.remove((22,3))
tup2.insert(1,(222,3))
tup2=tuple(tup2)
print(tup)
print(tup2)

#11.to convert string to tuple
a=input("Enter the string::")
print(a)
print(type(a))
a=a.replace(" ","")
a=tuple(a)
print("Tuple of the given string::",a)
print(type(a))

#12.to print tuple with string formatting
s=tuple(map(int,input("Enter the values for numeric tuple::").split(" ")))
print("this is a tuple::",s)

#13. to print a reversed tuple
s=tuple(map(str,input("Enter the values of tuple::").split(" ")))
s1=list(s)
s1.reverse()
s1=tuple(s1)
print("The normal tuple is-{} and the reversed tuple is-{}".format(s,s1))

#14.to unzip the tuple elements to individual lists
li=[]
s=tuple(map(str,input("Enter the values of tuple::").split(" ")))
print(s)
s=list(s)
for i in s:
    print(list(i))
